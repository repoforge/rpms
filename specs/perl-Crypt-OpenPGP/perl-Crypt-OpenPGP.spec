# $Id$
# Authority: dag
# Upstream: Benjamin Trott <cpan$stupidfool,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-OpenPGP

Summary: Pure-Perl OpenPGP implementation
Name: perl-Crypt-OpenPGP
Version: 1.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-OpenPGP/

Source: http://search.cpan.org/CPAN/authors/id/B/BT/BTROTT/Crypt-OpenPGP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(Crypt::Blowfish)
BuildRequires: perl(Crypt::CAST5_PP)
BuildRequires: perl(Crypt::DES_EDE3)
BuildRequires: perl(Crypt::DSA)
BuildRequires: perl(Crypt::IDEA)
BuildRequires: perl(Crypt::RIPEMD160)
BuildRequires: perl(Crypt::RSA)
BuildRequires: perl(Crypt::Rijndael)
BuildRequires: perl(Crypt::Twofish)
BuildRequires: perl(Data::Buffer) >= 0.04
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Digest::SHA1)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Math::Pari)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::Escape)
BuildRequires: perl >= 5.8.1
Requires: perl(Compress::Zlib)
Requires: perl(Crypt::Blowfish)
Requires: perl(Crypt::CAST5_PP)
Requires: perl(Crypt::DES_EDE3)
Requires: perl(Crypt::DSA)
Requires: perl(Crypt::IDEA)
Requires: perl(Crypt::RIPEMD160)
Requires: perl(Crypt::RSA)
Requires: perl(Crypt::Rijndael)
Requires: perl(Crypt::Twofish)
Requires: perl(Data::Buffer) >= 0.04
Requires: perl(Digest::MD5)
Requires: perl(Digest::SHA1)
Requires: perl(File::HomeDir)
Requires: perl(LWP::UserAgent)
Requires: perl(MIME::Base64)
Requires: perl(Math::Pari)
Requires: perl(URI::Escape)
Requires: perl >= 5.8.1

%filter_from_requires /^perl*/d
%filter_setup


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
%doc CREDITS Changes MANIFEST README 
%doc %{_mandir}/man3/Crypt::OpenPGP.3pm*
%doc %{_mandir}/man3/Crypt::OpenPGP::*.3pm*
%dir %{perl_vendorlib}/Crypt/
%{perl_vendorlib}/Crypt/OpenPGP/
%{perl_vendorlib}/Crypt/OpenPGP.pm

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 1.04-1
- Updated to version 1.04.

* Tue Aug 19 2008 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
