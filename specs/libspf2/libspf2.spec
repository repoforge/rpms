%lib_package spf2 2

Summary: An implemenation of the Sender Policy Framework
Name: libspf2
Version: 1.2.9
Release: 6%{?dist}
License: GPL/BSD dual license
Group: System Environment/Libraries
URL: http://www.libspf2.org/
Source0: http://www.libspf2.org/spf/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gettext, gcc-c++

%description
libspf2 implements the Sender Policy Framework, a part of the SPF/SRS
protocol pair. libspf2 is a library which allows email systems such as
Sendmail, Postfix, Exim, Zmailer and MS Exchange to check SPF records
and make sure that the email is authorized by the domain name that it
is coming from. This prevents email forgery, commonly used by
spammers, scammers and email viruses/worms.

%prep
%setup -q

%build
# The configure script checks for the existence of __ns_get16 and uses the
# system-supplied version if found, otherwise one from src/libreplace.
# However, this function is marked GLIBC_PRIVATE in recent versions of glibc
# and shouldn't be called even if the configure script finds it. So we make
# sure that the configure script always uses the version in src/libreplace.
# This prevents us getting an unresolvable dependency in the built RPM.
ac_cv_func___ns_get16=no
export ac_cv_func___ns_get16
%configure
make

%install
rm -rf %{buildroot}
%makeinstall includedir=%{buildroot}%{_includedir}/spf2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README LICENSES TODO
%{_bindir}/spf*

%changelog
* Tue Mar  1 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.2.9-6
- Update to 1.2.9.

* Tue Oct 25 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Fixes for 64 bits (by Carsten Koch-Mauthe <ckm@vienenbox.de>).

* Mon Jul  4 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.2.5.

* Fri Feb 11 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.
- added patches from builds of Paul Howarth <paul@city-fan.org>.
