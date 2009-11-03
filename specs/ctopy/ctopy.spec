# $Id$
# Authority: dag
# Upstream: Eric S. Raymond <esr$snark,thyrsus.com>

Summary: C to Python translator
Name: ctopy
Version: 1.0
Release: 2%{?dist}
License: BSD
Group: Development/Tools
URL: http://www.catb.org/~esr/ctopy/

Source: http://www.catb.org/~esr/ctopy/ctopy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

%description
ctopy automates the parts of translating C source code to Python
source code that are difficult for a human but easy for a
machine. This allows a human programmer to concentrate on the
nontrivial parts of the translation.

%prep 
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 ctopy %{buildroot}%{_bindir}/ctopy
%{__install} -Dp -m0644 ctopy.1 %{buildroot}%{_mandir}/man1/ctopy.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_mandir}/man1/ctopy.1*
%{_bindir}/ctopy

%changelog
* Sun Jan 21 2007 Dag Wieers <dag@wieers.com> - 1.0-2
- Fix group tag.

* Sat Oct 21 2006 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
