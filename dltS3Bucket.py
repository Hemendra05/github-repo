import boto3 
import argparse
import inquirer
import time
import re
from pprint import pprint
import os

my_parser = argparse.ArgumentParser(description="remove bucket")
my_parser.add_argument('--profile', type=str, help="profile to be used")



def main():
    args = my_parser.parse_args()
    profile = args.profile    

    session = boto3.Session(profile_name=profile)
    
    client = session.client('s3')
    s3 = session.resource('s3')

    res = client.list_buckets()
    buckets = [
        # "aspcarp-inpbdarbkd70c4aa0-15tdfljdhffrw",
        # "aspskip-inpbdarbkaspskic9367785-ux2bw3jt66ox",
        # "aspskip-inpbdarbkaspskic9367785-ymdzl4vm8gt",
        # "basparp-inpbdarbkbasparf29d1f3c-5p3pwmrdrsnz",
        # "cartrap-inpbdarbkcartra265be376-1h9ykc4hhs8mm",
        # "cartrap-inpbdarbkcartra265be376-qzkb33y08c7x",
        # "chastap-inpbdarbkchastae79f3c60-15c5bl46b9a7z",
        # "chastap-inpbdarbkchastae79f3c60-se659g1lfoci",
        # "clgautp-inpbdarbkclgaut080c63f3-1w3ofousotgk4",
        # "clgautp-inpbdarbkclgaut080c63f3-qsgjx3v1ey6y",
        # "datcolp-inpbdarbkdatcol20fdf197-1958nuqrw3pxz",
        # "datcolp-inpbdarbkdatcol20fdf197-1k4w3t4mgjedk",
        # "datcolp-inpbdarbkdatcol20fdf197-1m2nlil57dlo0",
        # "datcolp-inpbdarbkdatcol20fdf197-xlgk95drw6lc",
        # "falrnmpp-inpmywsprodbdarbkfalrnmc35effd2-wsccx1elxbn2",
        # "ftlrnmpp-inpmywsprodbdarbkftlrnm6dc31055-135w3g59hftan",
        # "graeazp-inpbdarbkgraeaz942a2f73-1a1oig9mx0jeb",
        # "graeazp-inpbdarbkgraeaz942a2f73-1fj2o4pxc7vzm",
        # "graeazp-inpbdarbkgraeaz942a2f73-1ltmhqp7snltg",
        # "graeazp-inpbdarbkgraeaz942a2f73-41mjx7bs5xkb",
        # "graeazp-inpbdarbkgraeaz942a2f73-cs39d9rlu67m",
        # "graeazp-inpbdarbkgraeaz942a2f73-eziwbm4p4oh",
        # "graeazp-inpbdarbkgraeaz942a2f73-j23xznk3adjj",
        # "graeazp-inpbdarbkgraeaz942a2f73-o658jkhmg1zo",
        # "graeazp-inpbdarbkgraeaz942a2f73-rxenmdvkpy5r",
        # "inthybp-inpbdarbkinthyb0733b54f-fji5cog5e0n0",
        # "inthybp-inpbdarbkinthyb0733b54f-iniw0qaekau1",
        # "intseap-inpbdarbkintsea641c7627-1al6qlkrasgcz",
        # "intseap-inpbdarbkintsea641c7627-f2kc89uqz6v0",
        # "lalrnmpp-inpmywsprodbdarbklalrnm6f265c87-6pha7sq659wx",
        # "lalrnmpp-inpmywsprodbdarbklalrnm6f265c87-r5o6d2j85441",
        # "linresp-inpbdarbklinresde8ed299-1bft7zpor2gg0",
        # "loadtestingstack-dltcommonresourceslogsbucket48a2-8c9tujkyivgx",
        # "loadtestingstack-dltconsoleresourcesdltcloudfront-1hkbyhdz2vltv",
        # "loadtestingstack-dlttestrunnerstoragedltscenarios-1nq5hn5pje1im",
        # "patinsp-inpbdarbkpatinsb29ad4ac-141g6ex3ztiuk",
        # "patinsp-inpbdarbkpatinsb29ad4ac-1o2nl6l7j894j",
        # "patinsp-inpbdarbkpatinsb29ad4ac-k2poaabzcpjq",
        # "patjdsp-inpbdarbkpatjdsee06a6c1-131czpmvf7tay",
        # "patjdsp-inpbdarbkpatjdsee06a6c1-1acv7jql5h3ac",
        # "patjdsp-inpbdarbkpatjdsee06a6c1-1c4ed475l1zhn",
        # "patresp-inpbdarbkpatres3a4ecb2d-14q51pbkxjkpa",
        # "patresp-inpbdarbkpatres3a4ecb2d-2l13vnk810jc",
        # "patresp-inpbdarbkpatres3a4ecb2d-e25rn7z8mvcm",
        # "pdlrnmpp-inpmywsprodbdarbkpdlrnm510b1f65-fcvjvjqlholr",
        # "rectmep-inpbdarbkrectmede689b8f-16327uvfsqo1d",
        # "rectmep-inpbdarbkrectmede689b8f-kvyyajhu6f0y",
        # "relskip-inpbdarbkrelski4b340899-1post8a7cvyg8",
        # "relskip-inpbdarbkrelski4b340899-gwwjyd8i0ews",
        # "resparp-inpbdarbkrespar3c87a408-cztgyp0aawnu",
        # "rqlrnmpp-inpmywsprodbdarbkrqlrnm51848ed7-1ragi2eimi56i",
        # "savcomp-inpbdarbksavcomb2f0cedf-1hp7b1xutkaie",
        # "savcomp-inpbdarbksavcomb2f0cedf-6vcp0ckyt6r",
        # "savcomp-inpbdarbksavcomb2f0cedf-zjx24ldp2oz9",
        # "savejdp-inpbdarbksavejdd8b6fc1a-1rgm3y55gy38v",
        # "savejdp-inpbdarbksavejdd8b6fc1a-i48fuhtz9h2a",
        # "savejdp-inpbdarbksavejdd8b6fc1a-qfsn9zl7fbue",
        # "savpatp-inpbdarbksavpate174ee38-hpo6duvme0tt",
        # "savpatp-inpbdarbksavpate174ee38-mly5gnsg6po0",
        # "savpatp-inpbdarbksavpate174ee38-ubtg8i3cdewa",
        "savresp-inpbdarbksavres3a7abc2d-119lt84850tuc",
        "savusep-inpbdarbksavuse8b29347b-1hxizrw71zrgq",
        "savusep-inpbdarbksavuse8b29347b-1r10dl6s8uonk",
        "savusep-inpbdarbksavuse8b29347b-ju5iggrbrrru",
        "sklautp-inpbdarbksklaut2e174c22-ehysgp3wglsc",
        "sklautp-inpbdarbksklaut2e174c22-elphd8daagcx",
        "tracamp-inpbdarbkd70c4aa0-1xeyuyvpmwqew",
        "tracamp-inpbdarbkd70c4aa0-nmzywqm4p6av",
        "trangsp-inpbdarbktrangs60f4a6ba-1edbkcp42mx30",
        "trangsp-inpbdarbktrangs60f4a6ba-r39xp751rb76",
        "tranodp-inpbdarbktranod8a4219aa-6noyfc3dqvov",
        "tranodp-inpbdarbktranod8a4219aa-94ktzt2nmy72",
        "tranodp-inpbdarbktranod8a4219aa-jgvvc1snfiyf",
        "tranodp-inpbdarbktranod8a4219aa-yg1yk2pc8f4k",
        "unetrap-inpbdarbkunetraafd12d47-1os4wya3o4rpe",
        "unetrap-inpbdarbkunetraafd12d47-33g51xvr1igk",
        "unlusep-inpbdarbkunlusee6ad0c5c-5w0x0xgvcn53",
        "unlusep-inpbdarbkunlusee6ad0c5c-ur5tlfwbehy8",
        "usetrap-inpbdarbkusetra209517fb-1e6fqjg5anjoy",
        "usetrap-inpbdarbkusetra209517fb-hq74h66i623s"
    ]


    questions = [
    inquirer.Checkbox('buckets',
                    message="Which buckets are you going to delete?",
                    choices=buckets
                    ),
    inquirer.Text('confirm',
                    message="Are you sure you want to delete the buckets? Type delete to confirm your actions",
                    validate=lambda _, x: re.match('^delete$', x)
                    )
    ]

    answer = inquirer.prompt(questions)
    print(answer)
    if len(answer['buckets'])>0 and answer['confirm'] == 'delete':          
        for bucket in answer['buckets']:
            print(f'deleting objects in bucket {bucket}...')
            content = client.list_objects(Bucket=bucket)
            if 'Contents' in content and len(content['Contents'])>0:
                objects = [{'Key':object['Key']} for object in content['Contents']]
                client.delete_objects(Bucket=bucket,Delete={'Objects':objects})
                time.sleep(3)
            
            print(f'removing object versions...')
            
            versions = client.list_object_versions(Bucket=bucket) # list all versions in this bucket
            if 'Versions' in versions and len(versions['Versions'])>0:
                s3_bucket = s3.Bucket(bucket)
                s3_bucket.object_versions.delete() # delete all versions
                time.sleep(1)

            print(f'deleting bucket {bucket}...')
            client.delete_bucket(Bucket=bucket) # delete bucket
            time.sleep(3)


if __name__ == '__main__':
    main()