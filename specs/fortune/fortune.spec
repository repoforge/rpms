# $Id$
# Authority: dries

%define DisableOffensiveFortunes 1

Summary: program which will display a fortune
Name: fortune
Version: 1.0
Release: 37.2%{?dist}
License: BSD
Group: Amusements/Games
# no URL found

Source: ftp://sunsite.unc.edu/pub/Linux/games/amusements/fortune/fortune-mod-9708.tar.gz
Source1: http://www.kernelnewbies.org/kernelnewbies-fortunes.tar.gz
Source2: bofh-excuses.tar.bz2
# http://www.splitbrain.org/./Fortunes/starwars/
Source3: http://www.splitbrain.org/Fortunes/starwars/fortune-starwars.tgz
# http://www.netmeister.org/misc.html
Source4: http://www.netmeister.org/apps/fortune-mod-futurama-0.2.tar.bz2
Source5: http://www.netmeister.org/apps/fortune-mod-calvin-0.1.1.tar.gz
# http://www.aboleo.net/software/index.ds
#  Zippy the Pinhead
Source6: fortune-zippy.tar.gz
#  Tao Te Ching
Source7: fortune-tao.tar.gz
# http://www.splitbrain.org/./Fortunes/hitchhiker/
Source8: http://www.splitbrain.org/Fortunes/hitchhiker/fortune-hitchhiker.tgz
# http://www.splitbrain.org/./Fortunes/simpsons/
Source9: http://www.splitbrain.org/Fortunes/simpsons/fortune-simpsons-chalkboard.tgz
# The Elements of Programming Style - fortune cookie is a fortune cookie
# file containing the 69 tips from the "Elements of Programming Style" by
# Kernighan & Plaugher.
Source10: http://db.ilug-bom.org.in/lug-authors/philip/misc/fortune-mod-prog-style.tar.gz
# http://www.splitbrain.org/./Fortunes/fgump/
Source11: http://www.splitbrain.org/Fortunes/fgump/fortune-fgump.tgz
# http://www.splitbrain.org/./Fortunes/discworld/
Source12: http://www.splitbrain.org/Fortunes/discworld/fortune-discworld.tgz
# http://www.splitbrain.org/./Fortunes/xfiles/
Source13: http://www.splitbrain.org/Fortunes/xfiles/fortune-xfiles.tgz
# http://www.schwarzvogel.de/software-misc.shtml
Source14: http://www.schwarzvogel.de/pkgs/kernelcookies-8.tar.gz
# http://dune.s31.pl/
Source15: fortune-mod-dune-quotes.2.0.1.tar.gz
# quotes of 'Comic Book Guy'
Source16: http://pinkemostar.com:8008/files/cbg-quotes.tar.gz
# Simpsons Ralph Wiggum Quotes is a 'fortune' quote file with quotes from
# the one, the only, Ralph Wiggum. This was inspired by the Quotable Homer
# fortune file.
Source17: http://www.pinkemostar.com:8008/files/ralph-quotes.tar.gz
# http://eol.init1.nl/linux/index.php   (southpark quotes)
#Source18: http://eol.init1.nl/linux/SP-0.1.tar.gz
Source18: http://eelco.is.a.rootboy.net/fortunecookies/SP-0.2.tar.gz
# http://freshmeat.net/redir/quotablehomerquotes/8751/url_homepage/homer.html
# homer simpson quotes
Source19: http://www.cs.indiana.edu/~crcarter/homer/homer-quotes.tar.gz
# Osho quotes
# http://www.geocities.com/avitiw/fortune.html
Source20: http://www.geocities.com/avitiw/fortune-osho-1.1.tar.gz
# http://eol.init1.nl/content/category/2/36/54/
Source21: http://eelco.is.a.rootboy.net/fortunecookies/powerpuff-0.3.tar.gz
# http://eol.init1.nl/content/category/2/36/54/
Source22: http://eelco.is.a.rootboy.net/fortunecookies/oneliners-0.1.tar.gz
# fortune macintosh
Source23: http://www.diablonet.net/~mercadal/projects/fortune/macintosh-1.3.tgz
# The Art of War Fortune Mod
Source24: http://www.de-brauwer.be/wastebasket/fortunes-taow-1.0.tar.gz

Obsoletes: fortune-mod < %{version}-%{release}
Provides:  fortune-mod = %{version}-%{release}

Patch0: fortune-mod-offense.patch
Patch1: fortune-mod-1.0-remove-offensive.patch
Patch2: fortune-mod-1.0-remove-offensive-option.patch
Patch3: known-as-dentists-typo.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Fortune-mod contains the ever-popular fortune program, which will
display quotes or witticisms. Fun-loving system administrators can add
fortune to users' .login files, so that the users get their dose of
wisdom each time they log in.

%prep
%setup -q -n fortune-mod-9708
#%setup -D -T -a 1 -n fortune-mod-9708
#%setup -D -T -a 2 -n fortune-mod-9708
%setup -D -T -a 3 -n fortune-mod-9708
%setup -D -T -a 4 -n fortune-mod-9708
%setup -D -T -a 5 -n fortune-mod-9708
%setup -D -T -a 6 -n fortune-mod-9708
%setup -D -T -a 7 -n fortune-mod-9708
%setup -D -T -a 8 -n fortune-mod-9708
%setup -D -T -a 9 -n fortune-mod-9708
%setup -D -T -a 10 -n fortune-mod-9708
%setup -D -T -a 11 -n fortune-mod-9708
%setup -D -T -a 12 -n fortune-mod-9708
%setup -D -T -a 13 -n fortune-mod-9708
%setup -D -T -a 14 -n fortune-mod-9708
%setup -D -T -a 15 -n fortune-mod-9708
%setup -D -T -a 16 -n fortune-mod-9708
%setup -D -T -a 17 -n fortune-mod-9708
%setup -D -T -a 18 -n fortune-mod-9708
%setup -D -T -a 19 -n fortune-mod-9708
%setup -D -T -a 20 -n fortune-mod-9708
%setup -D -T -a 21 -n fortune-mod-9708
%setup -D -T -a 22 -n fortune-mod-9708
%setup -D -T -a 23 -n fortune-mod-9708
%setup -D -T -a 24 -n fortune-mod-9708

%if %{DisableOffensiveFortunes}
%patch0 -p1 -b .disable-offensive1
%patch1 -p0 -b .disable-offensive2
%patch2 -p0 -b .remove-offensive-option
%patch3 -p1
%endif

%build
make COOKIEDIR=%{_datadir}/games/fortune \
	FORTDIR=%{_bindir} BINDIR=%{_sbindir}

%install
%{__rm} -rf %{buildroot}

make    COOKIEDIR=%{_datadir}/games/fortune fortune/fortune.man
make	FORTDIR=%{buildroot}/%{_bindir} \
	COOKIEDIR=%{buildroot}%{_datadir}/games/fortune \
	BINDIR=%{buildroot}/%{_sbindir} \
	BINMANDIR=%{buildroot}/%{_mandir}/man1 \
	FORTMANDIR=%{buildroot}/%{_mandir}/man6 \
	install

%{__cp} -p fortune-starwars/starwars fortune-starwars/starwars.dat %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p fortune-mod-futurama-0.2/futurama fortune-mod-futurama-0.2/futurama.dat %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p fortune-mod-calvin-0.1.1/calvin fortune-mod-calvin-0.1.1/calvin.dat %{buildroot}%{_datadir}/games/fortune/
mv fortune-zippy-0.2/zippy fortune-zippy-0.2/zippy2
(cd fortune-zippy-0.2; ../util/strfile zippy2)
%{__cp} -p fortune-zippy-0.2/zippy2 fortune-zippy-0.2/zippy2.dat %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p fortune-tao/tao fortune-tao/tao.dat %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p fortune-hitchhiker/hitchhiker fortune-hitchhiker/hitchhiker.dat %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p fortune-simpsons-chalkboard/chalkboard fortune-simpsons-chalkboard/chalkboard.dat %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p fortune-mod-prog-style/prog-style.dat fortune-mod-prog-style/prog-style %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p fortune-fgump/fgump fortune-fgump/fgump.dat %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p fortune-discworld/discworld.dat fortune-discworld/discworld %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p fortune-xfiles/xfiles.dat fortune-xfiles/xfiles %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p kernelcookies*/kernelcookies kernelcookies*/kernelcookies.dat %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p fortune-mod-dune-quotes.2.0.1/chapterhouse-dune fortune-mod-dune-quotes.2.0.1/children-of-dune fortune-mod-dune-quotes.2.0.1/dune-messiah \
  fortune-mod-dune-quotes.2.0.1/dune fortune-mod-dune-quotes.2.0.1/god-emperor fortune-mod-dune-quotes.2.0.1/house-atreides \
  fortune-mod-dune-quotes.2.0.1/house-harkonnen fortune-mod-dune-quotes.2.0.1/heretics-of-dune fortune-mod-dune-quotes.2.0.1/chapterhouse-dune.dat \
  fortune-mod-dune-quotes.2.0.1/children-of-dune.dat fortune-mod-dune-quotes.2.0.1/dune.dat fortune-mod-dune-quotes.2.0.1/dune-messiah.dat \
  fortune-mod-dune-quotes.2.0.1/god-emperor.dat fortune-mod-dune-quotes.2.0.1/heretics-of-dune.dat fortune-mod-dune-quotes.2.0.1/house-atreides.dat \
  fortune-mod-dune-quotes.2.0.1/house-harkonnen.dat %{buildroot}%{_datadir}/games/fortune/
%{__cp} cbg cbg.dat %{buildroot}%{_datadir}/games/fortune/
util/strfile ralph
%{__cp} ralph ralph.dat %{buildroot}%{_datadir}/games/fortune/
%if %{DisableOffensiveFortunes}
# southpark.. quite sure it's part of 'offensive'
%else
%{__cp} -p SP/SP SP/SP.dat %{buildroot}%{_datadir}/games/fortune/
%endif
%{__cp} -p fortune-homer/homer fortune-homer/homer.dat %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p osho.dat osho %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p powerpuff-*/powerpuff* %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p oneliners-0.1/oneliners* %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p macintosh/macintosh* %{buildroot}%{_datadir}/games/fortune/
%{__cp} -p fortunes-taow-1.0/taow* %{buildroot}%{_datadir}/games/fortune/

%{__tar} zxvf %{SOURCE1} -C %{buildroot}%{_datadir}/games/fortune/
%if %{DisableOffensiveFortunes}
%{__rm} %{buildroot}%{_datadir}/games/fortune/men-women*
%endif

# Using bzcat for portability because tar keeps randomly changing the switch
# for bzip.  It was "y" at one point, then "I", and now it is "j".  God knows
# WTF they'll change it too next.

bzcat %{SOURCE2} | %{__tar} xvf - -C %{buildroot}%{_datadir}/games/fortune/

# call strfile on all fortune files
%{__rm} -f %{buildroot}%{_datadir}/games/fortune/*.dat
(cd %{buildroot}%{_datadir}/games/fortune/; for i in *; do %{buildroot}%{_sbindir}/strfile ${i}; done)

%clean
%{__rm} -rf %{buildroot}

%package bofh-excuses
Summary: Fortune files with BOFH excuses
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description bofh-excuses
Some fortune BOFH excuses (BOFH = Bastard Operator From Hell)

%description -l nl bofh-excuses
Een aantal fortune BOFH excuses (BOFH = Bastard Operator From Hell)

%package kernelnewbies
Summary: Fortune files with kernelnewbies quotes
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description kernelnewbies
Some fortune quotes from kernelnewbies

%description -l nl kernelnewbies
Een aantal fortune kernelnewbies quotes

%package starwars
Summary: Fortune files with Starwars quotes
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description starwars
Some fortune quotes from the Starwars movies, downloaded from
http://www.splitbrain.org/./Fortunes/starwars/

%description -l nl starwars
Een aantal fortune quotes van de Starwars films, gedownload van
http://www.splitbrain.org/./Fortunes/starwars/

%package futurama
Summary: Fortune files with Futurama quotes
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description futurama
Some fortune quotes from Futurama, downloaded from
http://www.netmeister.org/misc.html

%description -l nl futurama
Enkele fortune quotes van Futurama, gedownload van
http://www.netmeister.org/misc.html

%package calvin
Summary: Fortune files with Calvin and Hobbes quotes
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description calvin
Some fortune quotes from Calvin and Hobbes, downloaded from
http://www.netmeister.org/misc.html

%description -l nl calvin
Enkele fortune quotes van Calvin en Hobbes, gedownload van
http://www.netmeister.org/misc.html

%package zippy2
Summary: Fortune files with Zippy the Pinhead quotes
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description zippy2
Some fortune quotes from Zippy the Pinhead, downloaded from
http://www.aboleo.net/software/misc/

%description -l nl zippy2
Enkele fortune quotes van Zippy the Pinhead, gedownload van
http://www.aboleo.net/software/misc/

%package tao
Summary: Fortune files with Tao Te Ching quotes
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description tao
Some fortune quotes from Tao Te Ching, downloaded from
http://www.aboleo.net/software/misc/

%description -l nl tao
Enkele fortune quotes van Tao Te Ching, gedownload van
http://www.aboleo.net/software/misc/

%package hitchhiker
Summary: Fortune files with quotes from Hitchhikers Guide to the Galaxy
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description hitchhiker
Some fortune quotes from Hitchhikers Guide to the Galaxy, downloaded from
http://www.splitbrain.org/./Fortunes/hitchhiker/

%description -l nl hitchhiker
Enkele fortune quotes van Hitchhikers Guide to the Galaxy, gedownload van
http://www.splitbrain.org/./Fortunes/hitchhiker/

%package simpsons-chalkboard
Summary: Fortune files with quotes from Bart Simpson's chalkboard-writings
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description simpsons-chalkboard
Some fortune quotes from Bart Simpson's chalkboard-writings, downloaded from
http://www.splitbrain.org/./Fortunes/simpsons/

%description -l nl simpsons-chalkboard
Enkele fortune quotes van Bart Simpson's chalkboard-writings, gedownload van
http://www.splitbrain.org/./Fortunes/simpsons/

%package prog-style
Summary: Fortune files with the 69 tips from the "Elements of Programming Style"
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description prog-style
Some fortune quotes from the 69 tips from the
"Elements of Programming Style" by Kernighan and Plaugher, downloaded from
http://freshmeat.net/redir/fortune-mod-prog-style/19342/url_tgz/fortune-mod-prog-style.tar.gz

%description -l nl prog-style
Enkele fortune quotes met de 69 tips van
"Elements of Programming Style" by Kernighan and Plaugher, gedownload van
http://freshmeat.net/redir/fortune-mod-prog-style/19342/url_tgz/fortune-mod-prog-style.tar.gz

%package fgump
Summary: Fortune files with quotes from the movie Forrest Gump
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description fgump
Some fortune quotes from the movie Forrest Gump, downloaded from
http://www.splitbrain.org/./Fortunes/fgump/

%description -l nl fgump
Enkele fortune quotes van de film Forrest gump, gedownload van
http://www.splitbrain.org/./Fortunes/fgump/

%package discworld
Summary: Fortune files with quotes from Discworld
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description discworld
Some fortune quotes from the novels of Discworld written
by Terry Pratchett, downloaded from
http://www.splitbrain.org/./Fortunes/discworld/

%description -l nl discworld
Enkele fortune quotes van de Discworld boeken geschreven
door Terry Pratchett, gedownload van
http://www.splitbrain.org/./Fortunes/discworld/

%package xfiles
Summary: Fortune files with quotes from The X-Files
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description xfiles
Some fortune quotes from The X-Files, downloaded from
http://www.splitbrain.org/./Fortunes/xfiles/

%description -l nl xfiles
Enkele fortune quotes van The X-Files, gedownload van
http://www.splitbrain.org/./Fortunes/xfiles/

%package kernelcookies
Summary: Fortune files with quotes from kernelcookies
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description kernelcookies
Some fortune quotes from kernelcookies, downloaded from
http://unattached.i-no.de/software-misc.shtml

%description -l nl kernelcookies
Enkele fortune quotes van kernelcookies, gedownload van
http://unattached.i-no.de/software-misc.shtml

%package dune
Summary: Fortune files with quotes from Dune
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description dune
Some fortune quotes from Dune, downloaded from
http://dune.s31.pl/

%description -l nl dune
Enkele fortune quotes van Dune, gedownload van
http://dune.s31.pl/

%package cbg
Summary: Fortune files with quotes from Comic Book Guy
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description cbg
Some fortune quotes from Comic Book Guy, downloaded from
http://freshmeat.net/redir/cbg-quotes/16138/url_tgz/cbg-quotes.tar.gz

%description -l nl cbg
Enkele fortune quotes van Comic Book Guy, gedownload van
http://freshmeat.net/redir/cbg-quotes/16138/url_tgz/cbg-quotes.tar.gz

%package simpsons-ralph
Summary: Fortune files with quotes from Comic Book Guy
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description simpsons-ralph
Some fortune quotes from Simpsons Ralph Wiggum, downloaded from
http://freshmeat.net/redir/ralph-quotes/16139/url_tgz/ralph-quotes.tar.gz

%description -l nl simpsons-ralph
Enkele fortune quotes van Simpsons Ralph Wiggum, gedownload van
http://freshmeat.net/redir/ralph-quotes/16139/url_tgz/ralph-quotes.tar.gz

%if %{DisableOffensiveFortunes}
# Soutpark will not be packaged.
%else
%package southpark
Summary: Fortune files with (offensive) quotes from Southpark
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description southpark
Some fortune quotes from Southpark, downloaded from
http://eol.init1.nl/linux/index.php

%description -l nl southpark
Enkele fortune quotes van Southpark, gedownload van
http://eol.init1.nl/linux/index.php
%endif

%package simpsons-homer
Summary: Fortune files with quotes from Homer Simpson
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description simpsons-homer
Some fortune quotes from Homer Simpson, downloaded from
http://freshmeat.net/redir/quotablehomerquotes/8751/url_homepage/homer.html

%description -l nl simpsons-homer
Enkele fortune quotes van Homer Simpson, gedownload van
http://freshmeat.net/redir/quotablehomerquotes/8751/url_homepage/homer.html

%package osho
Summary: Fortune files with quotes from the spiritual guru Osho
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description osho
Fortune files with quotes from the spiritual guru Osho, found at:
http://www.geocities.com/avitiw/fortune.html

%package powerpuff
Summary: Fortune files with quotes from the Power Puff Girls series
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description powerpuff
Fortune files with quotes from the Power Puff Girls series from Cartoon
Network, found at:
http://eol.init1.nl/content/category/2/36/54/

%package oneliners
Summary: Fortune files with quotes with random oneliners
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description oneliners
Fortune files with quotes with random oneliners, found at:
http://eol.init1.nl/content/category/2/36/54/

%package macintosh
Summary: Fortune files with quotes about macintoshes
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description macintosh
Fortune files with quotes about macintoshes, found at:
http://www.diablonet.net/~mercadal/projects/fortune/

%package taow
Summary: Fortune files with quotes from Sun Tzu's "The Art of War"
Group: Amusements/Games
Requires: fortune = %{version}-%{release}

%description taow
Fortune files with quotes from Sun Tzu's "The Art of War", made by Elie De
Brauwer.
http://www.de-brauwer.be/wiki/wikka.php?wakka=TheArtOfWar

%package all
Summary: Installs all fortune packages
Group: Amusements/Games
Requires: fortune = %{version}-%{release}
Requires: fortune-bofh-excuses = %{version}-%{release}
Requires: fortune-kernelnewbies = %{version}-%{release}
Requires: fortune-starwars = %{version}-%{release}
Requires: fortune-futurama = %{version}-%{release}
Requires: fortune-calvin = %{version}-%{release}
Requires: fortune-zippy2 = %{version}-%{release}
Requires: fortune-tao = %{version}-%{release}
Requires: fortune-hitchhiker = %{version}-%{release}
Requires: fortune-simpsons-chalkboard = %{version}-%{release}
Requires: fortune-prog-style = %{version}-%{release}
Requires: fortune-fgump = %{version}-%{release}
Requires: fortune-discworld = %{version}-%{release}
Requires: fortune-xfiles = %{version}-%{release}
Requires: fortune-kernelcookies = %{version}-%{release}
Requires: fortune-dune = %{version}-%{release}
Requires: fortune-cbg = %{version}-%{release}
Requires: fortune-simpsons-ralph = %{version}-%{release}
%if %{DisableOffensiveFortunes}
# Southpark will not be included
%else
Requires: fortune-southpark = %{version}-%{release}
%endif
Requires: fortune-simpsons-homer = %{version}-%{release}
Requires: fortune-osho = %{version}-%{release}
Requires: fortune-powerpuff = %{version}-%{release}
Requires: fortune-oneliners = %{version}-%{release}
Requires: fortune-macintosh = %{version}-%{release}
Requires: fortune-taow = %{version}-%{release}

%description all
All fortune packages will be installed if you install this package.

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README TODO
%{_bindir}/fortune
%{_sbindir}/strfile
%{_sbindir}/unstr
%{_datadir}/games/fortune/art*
%{_datadir}/games/fortune/ascii-art*
%{_datadir}/games/fortune/computers*
%{_datadir}/games/fortune/cookie*
%{_datadir}/games/fortune/definitions*
%{_datadir}/games/fortune/drugs*
%{_datadir}/games/fortune/education*
%{_datadir}/games/fortune/ethnic*
%{_datadir}/games/fortune/food*
%{_datadir}/games/fortune/fortunes*
%{_datadir}/games/fortune/goedel*
%{_datadir}/games/fortune/humorists*
%{_datadir}/games/fortune/kids*
%{_datadir}/games/fortune/law*
%{_datadir}/games/fortune/linuxcookie*
%{_datadir}/games/fortune/literature*
%{_datadir}/games/fortune/love*
%{_datadir}/games/fortune/magic*
%{_datadir}/games/fortune/medicine*
%{_datadir}/games/fortune/miscellaneous*
%{_datadir}/games/fortune/news*
%{_datadir}/games/fortune/people*
%{_datadir}/games/fortune/pets*
%{_datadir}/games/fortune/platitudes*
%{_datadir}/games/fortune/politics*
%{_datadir}/games/fortune/riddles*
%{_datadir}/games/fortune/science*
%{_datadir}/games/fortune/songs-poems*
%{_datadir}/games/fortune/sports*
%{_datadir}/games/fortune/startrek*
%{_datadir}/games/fortune/translate-me*
%{_datadir}/games/fortune/wisdom*
%{_datadir}/games/fortune/work*
%{_datadir}/games/fortune/zippy
%{_datadir}/games/fortune/zippy.dat
%dir %{_datadir}/games/fortune
%{_mandir}/man*/*

%files bofh-excuses
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/bofh-excuses*

%files kernelnewbies
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/kernelnewbies*

%files starwars
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/starwars*

%files futurama
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/futurama*

%files calvin
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/calvin*

%files zippy2
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/zippy2*

%files tao
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/tao*

%files hitchhiker
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/hitchhiker*

%files simpsons-chalkboard
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/chalkboard*

%files prog-style
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/prog-style*

%files fgump
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/fgump*

%files discworld
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/discworld*

%files xfiles
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/xfiles*

%files kernelcookies
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/kernelcookies*

%files dune
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/dune*
%{_datadir}/games/fortune/chapterhouse*
%{_datadir}/games/fortune/children-of-dune*
%{_datadir}/games/fortune/god-emperor*
%{_datadir}/games/fortune/heretics-of-dune*
%{_datadir}/games/fortune/house-atreides*
%{_datadir}/games/fortune/house-harkonnen*

%files cbg
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/cbg*

%files simpsons-ralph
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/ralph*

%if %{DisableOffensiveFortunes}
# Southpark will not be packaged
%else
%files southpark
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/SP*
%endif

%files simpsons-homer
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/homer*

%files osho
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/osho*

%files oneliners
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/oneliners*

%files powerpuff
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/powerpuff*

%files macintosh
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/macintosh*

%files taow
%defattr(-, root, root, 0755)
%{_datadir}/games/fortune/taow*

%files all
%defattr(-, root, root, 0755)

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-37.2
- Rebuild for Fedora Core 5.

* Wed Aug 31 2005 Dries Verachtert <dries@ulyssis.org> 1.0-37
- Quotes from Sun Tzu's "The Art of War" added, made by Elie De Brauwer.

* Sun Jul 03 2005 Dries Verachtert <dries@ulyssis.org> 1.0-36
- Apply strfile to all fortune files.

* Tue Mar 08 2005 Dries Verachtert <dries@ulyssis.org> 1.0-35
- Added macintosh quotes
- New url for Tao quotes
- Updated macintosh quotes to 1.3

* Sun Jan 02 2005 Dries Verachtert <dries@ulyssis.org> 1.0-33
- Fixed a grammatical error found by Greg Hogan.

* Sat Dec 04 2004 Rex Dieter 1.0-33
- Use versioned Obsoletes/Provides: fortune-mod.
- Add ownership %%_datadir/games/fortune.
- Get rid of %%_prefix/games/fortune symlink: fixes upgrade issues
  from fortune-mod.

* Wed Nov 24 2004 Dries Verachtert <dries@ulyssis.org> 1.0-32
- Added the Provides: fortune-mod (thanks to Jeff Pitman & Rex Dieter)
- Update of powerpuff quotes
- moved the binary to /usr/bin/

* Mon Oct 25 2004 Dries Verachtert <dries@ulyssis.org> 1.0-31
- Update of South Park quotes
- Added oneliners & powerpuff

* Mon Jun 21 2004 Dries Verachtert <dries@ulyssis.org> 1.0-30
- Update of the kernelcookies to version 8 with 80 new
  cookies from the 2.6.6 kernel tree.
- Added a subpackage 'all' which requires all the other
  subpackages.
- Osho quotes updated.

* Sat May 1 2004 Dries Verachtert <dries@ulyssis.org> 1.0-29
- added quotes found on freshmeat: quotes from the spiritual
  guru Osho.

* Thu Apr 22 2004 Dries Verachtert <dries@ulyssis.org> 1.0-28
- spec cleanup, fix file ownerships

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 1.0-27
- a bit of cleanup in the spec file

* Mon Dec 29 2003 Dries Verachtert <dries@ulyssis.org> 1.0-26
- added quite a lot of subpackages with more quotes

* Sun Dec 21 2003 Dries Verachtert <dries@ulyssis.org> 1.0-25
- first rebuild for Fedora Core 1
- renamed from fortune-mod to fortune
- updated the Source: tag to correct location

* Thu Aug 22 2002 Mike A. Harris <mharris@redhat.com> 1.0-24
- Removed -o option from fortune, the manpage and --help message, as
  we do not provide or support the offensive fortunes for obvious
  reasons.  (#54713)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 21 2002 Mike A. Harris <mharris@redhat.com> 1.0-21
- Bump release + rebuild.

* Mon Feb 25 2002 Mike A. Harris <mharris@redhat.com> 1.0-20
- Conditionalized previous change, and rebuilt in new build environment

* Tue Jan 29 2002 Preston Brown <pbrown@redhat.com>
- more editorial work

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Dec 23 2001 Mike A. Harris <mharris@redhat.com> 1.0-17
- Added bofh-excuses and kernelnewbies fortune files

* Tue Sep  4 2001 Mike A. Harris <mharris@redhat.com> 1.0-16
- Remove an offensive remark.
- s/Copyright/License/
- Fix buildroot line.

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun  6 2000 Bill Nottingham <notting@redhat.com>
- rebuild; FHS stuff

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Fri Jun 25 1999 Guido Flohr <gufl0000@stud.uni-sb.de>
- create fortune manpage without buildroot before installation

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 9)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- rebuilt for 6.0

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- new version
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
