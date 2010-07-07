# $Id$
# Authority: dag

Summary: Command Line XML Toolkit
Name: xmlstarlet
Version: 1.0.1
Release: 1%{?dist}
License: MIT
Group: Applications/Text
URL: http://xmlstar.sourceforge.net/

Source: http://dl.sf.net/xmlstar/xmlstarlet-%{version}.tar.gz
Patch0: xmlstarlet-1.0.1-nostatic.patch
Patch1: xmlstarlet-1.0.1-cmdname.patch
Patch2: xmlstarlet-1.0.1-docs.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libxml2-devel >= 2.6.12
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
%patch0 -p1 -b .nostatic
%patch1 -p1 -b .cmdname
%patch2 -p1 -b .docs

pushd doc
xmlto man xmlstarlet-man.xml
xmlto html-nochunks xmlstarlet-ug.xml
./gen-doc >xmlstarlet.txt
popd

%build
autoreconf -i
%configure
%{__make} %{?_smp_mflags}

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
* Wed Jun 30 2010 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Initial package. (using DAR)
