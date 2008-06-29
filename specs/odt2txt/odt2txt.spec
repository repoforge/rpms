# $Id$
# Authority: dries
# Upstream: Dennis Stosberg <dennis$stosberg,net>

Summary: Extract text from OpenDocument Text files
Name: odt2txt
Version: 0.4
Release: 1
License: GPL
Group: Applications/Text
URL: http://stosberg.net/odt2txt/

Source: http://stosberg.net/odt2txt/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
odt2txt extracts the text out of OpenDocument Texts. It is small, fast and 
portable, can output the document in your console encoding, and has very 
few external dependencies.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D odt2txt %{buildroot}%{_bindir}/odt2txt

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc GPL-2
%{_bindir}/odt2txt

%changelog
* Sun Jun 29 2008 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Updated to release 0.4.

* Mon Jun 25 2007 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Updated to release 0.3.

* Sun Jan 07 2007 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Updated to release 0.2.

* Sat Dec 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.
