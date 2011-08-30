%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Authen-OATH

Summary: OATH One Time Passwords
Name: perl-%{real_name}
Version: 1.0.0
Release: 1%{?dist}
License: GPL or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/dist/Authen-OATH/

Source0: http://search.cpan.org/CPAN/authors/id/S/SI/SIFUKURT/Authen-OATH-v1.0.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
BuildRequires: perl
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Digest::HMAC)
Requires: perl(Math::BigInt)
Requires: perl(Moose)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
The "Authen::OATH" module implements the HOTP and TOTP One Time
Password algorithms as defined by OATH, which is documented at
http://www.openauthentication.org.

All necessary parameters are set by default, though these can be
overridden. Both totp() and htop() have passed all of the test
vectors defined in the RFC documents for TOTP and HOTP.

The methods implemented by this module can verify logins for Google
Authenticator.

%prep
%setup -q -n %{real_name}-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} pure_install
find $RPM_BUILD_ROOT -type f -name .packlist -exec %{__rm} -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check || :
make test

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc Changes README
%{perl_vendorlib}/Authen/OATH.pm
%{_mandir}/man3/*.3*

%changelog
* Tue Aug 30 2011 Todd Lyons <tlyons@ivenue.com> - 0:1.0.0-1iv
- Initial package.
