# $Id$
# Authority: dag
# Upstream: Benjamin Trott <cpan$stupidfool,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-OpenPGP

Summary: Pure-Perl OpenPGP implementation
Name: perl-Crypt-OpenPGP
Version: 1.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-OpenPGP/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-OpenPGP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(Crypt::Blowfish)
BuildRequires: perl(Crypt::CAST5_PP)
BuildRequires: perl(Crypt::DSA)
BuildRequires: perl(Crypt::IDEA)
BuildRequires: perl(Crypt::Rijndael)
BuildRequires: perl(Crypt::RIPEMD160)
BuildRequires: perl(Crypt::RSA)
BuildRequires: perl(Crypt::Twofish)
BuildRequires: perl(Data::Buffer) >= 0.04
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Math::Pari)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(URI::Escape)

%description
Pure-Perl OpenPGP implementation.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS Changes MANIFEST README SIGNATURE ToDo
%doc %{_mandir}/man3/Crypt::OpenPGP.3pm*
%doc %{_mandir}/man3/Crypt::OpenPGP::*.3pm*
%dir %{perl_vendorlib}/Crypt/
%{perl_vendorlib}/Crypt/OpenPGP/
%{perl_vendorlib}/Crypt/OpenPGP.pm

%changelog
* Tue Aug 19 2008 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
