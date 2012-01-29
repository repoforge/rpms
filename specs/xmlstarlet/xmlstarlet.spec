# $Id$
# Authority: dag

%define _default_patch_fuzz 2

Summary: Command Line XML Toolkit
Name: xmlstarlet
Version: 1.3.0
Release: 1%{?dist}
License: MIT
Group: Applications/Text
URL: http://xmlstar.sourceforge.net/

Source: http://dl.sf.net/xmlstar/xmlstarlet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libxml2-devel >= 2.6.27
BuildRequires: libxslt-devel >= 1.1.9
BuildRequires: xmlto

%description
XMLStarlet is a set of command line utilities which can be used
to transform, query, validate, and edit XML documents and files
using simple set of shell commands in similar way it is done for
plain text files using UNIX grep, sed, awk, diff, patch, join, etc
commands.

%prep
%setup

### Rewrite xml reference to xmlstarlet
%{__perl} -pi.orig -e 's|^(bin_PROGRAMS =) .*$|$1 xmlstarlet|' Makefile*
%{__perl} -pi.orig -e 's|\bxml(\s)|xmlstarlet$1|g' Makefile* xmlstarlet.spec* src/*.c
%{__perl} -pi.orig -e 's|\bxml(\s)|xmlstarlet$1|g' doc/gen-doc doc/*.xml

pushd doc
xmlto man xmlstarlet-man.xml
xmlto html-nochunks xmlstarlet-ug.xml
./gen-doc >xmlstarlet.txt
popd

%build
%configure --disable-static-libs
%{__make} %{?_smp_mflags} EXEEXT="starlet"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog Copyright NEWS README TODO
%doc doc/xmlstarlet.txt doc/xmlstarlet-ug.html
%doc %{_mandir}/man1/xmlstarlet.1*
%{_bindir}/xmlstarlet

%changelog
* Mon Oct 10 2011 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Updated to release 1.3.0.

* Tue Jul 19 2011 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Tue Jun 07 2011 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

* Mon Apr 04 2011 Dag Wieers <dag@wieers.com> - 1.1.0-1
- Updated to release 1.1.0.

* Mon Mar 14 2011 Dag Wieers <dag@wieers.com> - 1.0.6-1
- Updated to release 1.0.6.

* Thu Feb 17 2011 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.

* Wed Jan 26 2011 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0.4.

* Wed Jun 30 2010 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Initial package. (using DAR)
