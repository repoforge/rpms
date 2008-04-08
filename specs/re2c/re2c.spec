# $Id$
# Authority: dag

Summary: Tool for generating C-based recognizers from regular expressions
Name: re2c
Version: 0.13.4
Release: 1
License: MIT
Group: Development/Tools
URL: http://re2c.sourceforge.net/

Source: http://dl.sf.net/re2c/re2c-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
re2c is a great tool for writing fast and flexible lexers. It has
served many people well for many years and it deserves to be
maintained more actively. re2c is on the order of 2-3 times faster
than a flex based scanner, and its input model is much more
flexible.

%prep
%setup

%build
%configure
%{__make} re2c

### Regenerate file scanner.cc
./re2c -b scanner.re >scanner.cc
%{__rm} -f re2c scanner.o
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 re2c %{buildroot}%{_bindir}/re2c
%{__install} -Dp -m0644 re2c.1 %{buildroot}%{_mandir}/man1/re2c.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG README doc/* examples/ lessons/
%doc %{_mandir}/man1/re2c.1*
%{_bindir}/re2c

%changelog
* Tue Apr 08 2008 Dag Wieers <dag@wieers.com> - 0.13.4-1
- Updated to release 0.13.4.

* Sat Feb 16 2008 Dag Wieers <dag@wieers.com> - 0.13.2-1
- Updated to release 0.13.2.

* Wed Sep 12 2007 Dag Wieers <dag@wieers.com> - 0.13.1-1
- Updated to release 0.13.1.

* Mon Jun 25 2007 Dag Wieers <dag@wieers.com> - 0.13.0-1
- Updated to release 0.13.0.

* Wed May 23 2007 Dag Wieers <dag@wieers.com> - 0.12.1-1
- Updated to release 0.12.1.

* Thu May 03 2007 Dag Wieers <dag@wieers.com> - 0.12.0-1
- Initial version.
