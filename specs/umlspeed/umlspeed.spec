# $Id$
# Authority: dag

Summary: Compiler for C-style language of UML notation
Name: umlspeed
Version: 0.15
Release: 1
License: GPL
Group: Development/Languages
URL: http://umlspeed.sourceforge.net/

Source: http://dl.sf.net/umlspeed/umlspeed-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-java

%description
UMLSpeed is a compiler for a C-style language of UML notation. It can produce
SVG UML diagrams, XMI documents and generate source code in various languages.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__make} install BIN_DIR="%{buildroot}%{_bindir}" MAN_DIR="%{buildroot}%{_mandir}/man1"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README TODO doc/ samples/
%doc %{_mandir}/man1/umlspeed.1*
%{_bindir}/umlspeed

%changelog
* Thu May 17 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Initial package. (using DAR)
