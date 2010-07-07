# $Id$
# Authority: dag

Summary: XML command-line tools
Name: xmlclitools
Version: 1.61
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://robur.slu.se/jensl/xmlclitools/

Source: http://robur.slu.se/jensl/xmlclitools/history/xmlclitools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-boot

BuildRequires: glib-devel
BuildRequires: libxml2-devel
Requires: glib
Requires: libxml2

%description
xmlclitools provides four command-line tools for searching, modifying,
and formating XML data. The tools are designed to work in conjunction
with standard *nix utilities such as grep, sort, and shell scripts.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 xmlfmt %{buildroot}%{_bindir}/xmlfmt
%{__install} -Dp -m0755 xmlgrep %{buildroot}%{_bindir}/xmlgrep
%{__install} -Dp -m0755 xmlmod %{buildroot}%{_bindir}/xmlmod
%{__install} -Dp -m0755 xmlngrep %{buildroot}%{_bindir}/xmlngrep
%{__install} -Dp -m0644 xmlfmt.1 %{buildroot}%{_mandir}/man1/xmlfmt.1
%{__install} -Dp -m0644 xmlgrep.1 %{buildroot}%{_mandir}/man1/xmlgrep.1
%{__install} -Dp -m0644 xmlmod.1 %{buildroot}%{_mandir}/man1/xmlmod.1
%{__install} -Dp -m0644 xmlgrep.1 %{buildroot}%{_mandir}/man1/xmlngrep.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING HACKING INSTALL MAINTAINER MANUAL README TODO *.txt test.xml*
%doc %{_mandir}/man1/xmlfmt.1*
%doc %{_mandir}/man1/xmlgrep.1*
%doc %{_mandir}/man1/xmlmod.1*
%doc %{_mandir}/man1/xmlngrep.1*
%{_bindir}/xmlgrep
%{_bindir}/xmlfmt
%{_bindir}/xmlmod
%{_bindir}/xmlngrep

%changelog
* Wed Jul 07 2010 Dag Wieers <dag@wieers.com> - 1.61-1
- Initial package. (using DAR)
