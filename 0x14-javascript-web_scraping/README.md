<img src="https://blog.holbertonschool.com/wp-content/uploads/2020/04/unnamed-2.png" width="170" height="210">

# Holbertonschool-higher_level_programming

## 0x14-javascript-web_scraping

## Lenguage
<img src="https://img.icons8.com/color/100/000000/javascript--v1.png"/> <img src="https://img.icons8.com/color/100/000000/nodejs.png"/>

## Learn Objetives
- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use axios and fetch API
- How to read and write a file using fs module

## Resources
- [Working with JSON data](https://intranet.hbtn.io/rltoken/RmDpb2gJfPrMar05QdxYvw)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.hbtn.io/rltoken/ibqGcS_YNbtWO8nPIlM2Ug)
- [Axios module](https://intranet.hbtn.io/rltoken/ZCxiaIcuRl3IlEL_VgGqoA)
- [Modern JS](https://intranet.hbtn.io/rltoken/Zf5LCjoTEuIXWWxoH_dGVQ)


## Requirements
-Javascripts interpretted on [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/) using [node v6.10.2](https://nodejs.org/en/blog/release/v6.10.2/) and must conform to [semistandard](https://github.com/Flet/semistandard) style.
- The first line of all your files should be exactly #!/usr/bin/node

## Installation

To use, first download  this repository into your local machine by issuing the following command in your local terminal. 
```
$ git clone https://github.com/Matilop15/holbertonschool-higher_level_programming.git
```
and 
```
$ cd 0x14-javascript-web_scraping
```

## Usage
### If you don't have Nodejs installed
```
$ sudo apt-get install -y nodejs
```

```
$ ./<filename.js> argument
```

## Files and Examples
[0-readme.js](0-readme.js)

Write a script that reads and prints the content of a file.
```
0x14-javascript-web_scraping:$ ./0-readme.js cisfun
C is super fun!
0x14-javascript-web_scraping:$ cat cisfun
C is super fun!
0x14-javascript-web_scraping:$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
```
[1-writeme.js](1-writeme.js)

Write a script that writes a string to a file.
```
0x14-javascript-web_scraping:$ ./1-writeme.js my_file.txt "Python is cool"
0x14-javascript-web_scraping:$ cat my_file.txt ; echo ""
Python is cool
```
[2-statuscode.js](2-statuscode.js)

Write a script that display the status code of a GET request.
```
0x14-javascript-web_scraping:$ ./2-statuscode.js https://intranet.hbtn.io/status
code: 200
0x14-javascript-web_scraping:$ ./2-statuscode.js https://intranet.hbtn.io/doesnt_exist
code: 404
```
[3-starwars_title.js](3-starwars_title.js)

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
```
0x14-javascript-web_scraping:$ ./3-starwars_title.js 1
A New Hope
0x14-javascript-web_scraping:$ ./3-starwars_title.js 5
Attack of the Clones
```
[4-starwars_count.js](4-starwars_count.js)

Write a script that prints the number of movies where the character “Wedge Antilles” is present.
```
0x14-javascript-web_scraping:$ ./4-starwars_count.js http://swapi.co/api/films
3
```
[5-request_store.js](5-request_store.js)

Write a script that gets the contents of a webpage and stores it in a file.
```
0x14-javascript-web_scraping:$ ./5-request_store.js http://loripsum.net/api loripsum
0x14-javascript-web_scraping:$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>
<p>Ad eos igitur converte te, quaeso. Pudebit te, inquam, illius tabulae, quam Cleanthes sane commode verbis depingere solebat. Sic enim censent, oportunitatis esse beate vivere. Quo studio Aristophanem putamus aetatem in litteris duxisse? Aeque enim contingit omnibus fidibus, ut incontentae sint. Ut aliquid scire se gaudeant? Qui enim existimabit posse se miserum esse beatus non erit. Putabam equidem satis, inquit, me dixisse. </p>
<p>Duo Reges: constructio interrete. Quid ei reliquisti, nisi te, quoquo modo loqueretur, intellegere, quid diceret? Quis animo aequo videt eum, quem inpure ac flagitiose putet vivere? Illud non continuo, ut aeque incontentae. Illa videamus, quae a te de amicitia dicta sunt. At ille pellit, qui permulcet sensum voluptate. Tamen aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si ista mala sunt, placet. </p>
<p>Non enim, si omnia non sequebatur, idcirco non erat ortus illinc. Nos cum te, M. Quem si tenueris, non modo meum Ciceronem, sed etiam me ipsum abducas licebit. Apparet statim, quae sint officia, quae actiones. Ergo instituto veterum, quo etiam Stoici utuntur, hinc capiamus exordium. Eadem nunc mea adversum te oratio est. Quid, si etiam iucunda memoria est praeteritorum malorum? Hoc enim constituto in philosophia constituta sunt omnia. </p>
```
[6-completed_tasks.js](6-completed_tasks.js)

Write a script that computes the number of tasks completed by user id.
```
0x14-javascript-web_scraping:$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
```

## Author
- [Matias López](https://uy.linkedin.com/in/matias-l%C3%B3pez-777796194?trk=people-guest_people_search-card)
