# $Id$
# Authority: shuff

%define langpack_version 2.00

Summary: Raw OCR Engine 
Name: tesseract
Version: 2.04
Release: 1%{?dist}
License: ASL 2.0
Group: Applications/Text
URL: http://code.google.com/p/tesseract-ocr/

Source0: http://tesseract-ocr.googlecode.com/files/%{name}-%{version}.tar.gz
Source1: http://tesseract-ocr.googlecode.com/files/%{name}-%{langpack_version}.fra.tar.gz
Source2: http://tesseract-ocr.googlecode.com/files/%{name}-%{langpack_version}.ita.tar.gz
Source3: http://tesseract-ocr.googlecode.com/files/%{name}-%{langpack_version}.nld.tar.gz
Source4: http://tesseract-ocr.googlecode.com/files/%{name}-%{langpack_version}.spa.tar.gz
Source5: http://tesseract-ocr.googlecode.com/files/%{name}-%{langpack_version}.eng.tar.gz
Source6: http://tesseract-ocr.googlecode.com/files/%{name}-%{langpack_version}.deu.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc-c++, make
BuildRequires: libtiff-devel

%package devel
Summary: Headers and development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

# it's too bad that these subpackages can't be noarch,
# but that needs rpm >= 4.6.0
%package fr
Summary: French langpack for %{name}
Group: Applications/File
Requires: %{name} >= %{langpack_version}

%package it
Summary: Italian langpack for %{name}
Group: Applications/File
Requires: %{name} >= %{langpack_version}

%package nl
Summary: Dutch langpack for %{name}
Group: Applications/File
Requires: %{name} >= %{langpack_version}

%package es
Summary: Spanish langpack for {name}
Group: Applications/File
Requires: %{name} >= %{langpack_version}

%package en
Summary: English langpack for {name}
Group: Applications/File
Requires: %{name} >= %{langpack_version}

%package de
Summary: German langpack for %{name}
Group: Applications/File
Requires: %{name} >= %{langpack_version}

%description
A commercial-quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005.

%description devel
Install this package if you want to compile programs that depend on tesseract.

%description fr
French language data for %{name}.

%description it
Italian language data for %{name}.

%description nl
Dutch language data for %{name}.

%description es
Spanish language data for %{name}.

%description en
English language data for %{name}.

%description de
German language data for %{name}.

%prep
%setup -q
%setup -q -a 1 -a 2 -a 3 -a 4 -a 5 -a 6

%build
sed -i 's#-DTESSDATA_PREFIX=@datadir@/#-DTESSDATA_PREFIX=@datadir@/%{name}/##' ccutil/Makefile.*
find . -type f -exec sed -i 's/#include <string>/#include <string>\n#include <cstring>/' {} \; ;
sed -i 's/#include <iostream>/#include <iostream>\n#include <cstring>/' viewer/svmnode.cpp
sed -i 's/#include <cstring>/#include <cstring>\n#include <cstdlib>/' viewer/svutil.cpp
sed -i 's/#include <cstring>/#include <cstring>\n#include <climits>/' viewer/scrollview.cpp
rm -f java/makefile
%configure
make %{?_smp_mflags} CPPFLAGS='-fno-strict-aliasing' 

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/%{name}
mv %{buildroot}%{_datadir}/tessdata %{buildroot}%{_datadir}/%{name}/
rm -rf %{buildroot}%{_libdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS phototest.tif README 
%{_bindir}/*
%dir %{_datadir}/tesseract/tessdata/
%{_datadir}/tesseract/tessdata/configs
%{_datadir}/tesseract/tessdata/confsets
%{_datadir}/tesseract/tessdata/tessconfigs

%files devel
%defattr(-,root,root,-)
%{_includedir}/tesseract

%files fr
%defattr(-,root,root,-)
%{_datadir}/tesseract/tessdata/fra*

%files it
%defattr(-,root,root,-)
%{_datadir}/tesseract/tessdata/ita*

%files nl
%defattr(-,root,root,-)
%{_datadir}/tesseract/tessdata/nld*

%files es
%defattr(-,root,root,-)
%{_datadir}/tesseract/tessdata/spa*

%files de
%defattr(-,root,root,-)
%{_datadir}/tesseract/tessdata/deu*

%files en
%defattr(-,root,root,-)
%{_datadir}/tesseract/tessdata/eng*

%changelog
* Fri May 14 2010 Steve Huff <shuff@vecna.org> - 2.04-1
- Updated to version 2.04.
- Modified to RPMforge style.
- Pulled in langpacks as subpackages.

* Tue Jun 24 2008 Alberto Lusiani <alusiani at gmail.com> - 2.03-1.co5.alu.1
- remove english OCR data, put them in a separate package
* Sun May 04 2008 Karol Trzcionka <karlikt at gmail.com> - 2.03-1
- Update to v2.03
* Sat Feb 09 2008 Karol Trzcionka <karlikt at gmail.com> - 2.01-2
- Rebuild for gcc43
* Fri Sep 07 2007 Karol Trzcionka <karlikt at gmail.com> - 2.01-1
- Upgrade to v2.01
* Tue Aug 21 2007 Karol Trzcionka <karlikt at gmail.com> - 2.00-1
- Upgrade to v2.00
* Thu Mar 22 2007 Karol Trzcionka <karlikt at gmail.com> - 1.04-1
- Change url and source
- Update to v1.04
- Make patch bases on upstream's v1.04b
- Change compilefix patch
- Adding -devel subpackage
* Thu Mar 22 2007 Karol Trzcionka <karlikt at gmail.com> - 1.03-2
- Including patch bases on cvs
* Tue Feb 13 2007 Karol Trzcionka <karlikt at gmail.com> - 1.03-1
- Update to v1.03
* Sat Jan 26 2007 Karol Trzcionka <karlikt at gmail.com> - 1.02-3
- Update BRs
- Fix x86_64 compile
* Sat Dec 30 2006 Karol Trzcionka <karlikt at gmail.com> - 1.02-2
- Fixed rpmlint warning in SRPM
* Fri Dec 29 2006 Karol Trzcionka <karlikt at gmail.com> - 1.02-1
- Initial Release
