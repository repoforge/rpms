# $Id$
# Authority: dag

Summary: Compiler for C-style language of UML notation
Name: umlspeed
Version: 0.19
Release: 1%{?dist}
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

### FIXME: Install the VIM syntax files 'somewhere'
#%{__install} -Dp -m0644 syntax/filetype.vim %{buildroot}%{_datadir}/vim/vimXX/syntax/filetype.vim
#%{__install} -Dp -m0644 syntax/umlspeed.vim %{buildroot}%{_datadir}/vim/vimXX/syntax/umlspeed.vim

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README TODO doc/ samples/
%doc %{_mandir}/man1/umlspeed.1*
%{_bindir}/umlspeed

%changelog
* Fri May 02 2008 Dag Wieers <dag@wieers.com> - 0.19-1
- Updated to release 0.19.

* Thu Jul 19 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Sat Jun 09 2007 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Wed May 23 2007 Dag Wieers <dag@wieers.com> - 0.16-1
- Updated to release 0.16.

* Thu May 17 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Initial package. (using DAR)
