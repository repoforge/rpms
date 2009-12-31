# $Id$
# Authority: dag
# Upstream: Mark Stosberg <mark$summersault,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-FormValidator

Summary: Validates user input (usually from an HTML form) based on input profile
Name: perl-Data-FormValidator
Version: 4.65
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-FormValidator/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARKSTOS/Data-FormValidator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(CGI) >= 3.48
BuildRequires: perl(Date::Calc) >= 5
BuildRequires: perl(Email::Valid)
BuildRequires: perl(File::MMagic) >= 1.17
BuildRequires: perl(Image::Size)
BuildRequires: perl(MIME::Types) >= 1.005
BuildRequires: perl(Module::Build)
BuildRequires: perl(Perl6::Junction) >= 1.1
BuildRequires: perl(Regexp::Common)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(overload)
BuildRequires: perl >= 5.008
Requires: perl(Date::Calc) >= 5
Requires: perl(Email::Valid)
Requires: perl(File::MMagic) >= 1.17
Requires: perl(Image::Size)
Requires: perl(MIME::Types) >= 1.005
Requires: perl(Perl6::Junction) >= 1.1
Requires: perl(Regexp::Common)
Requires: perl(Scalar::Util)
Requires: perl(Test::More)
Requires: perl(overload)
Requires: perl >= 5.008

%filter_from_requires /^perl*/d
%filter_setup

%description
Validates user input (usually from an HTML form) based
on input profile.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README RELEASE_NOTES
%doc %{_mandir}/man3/Data::FormValidator.3pm*
%doc %{_mandir}/man3/Data::FormValidator::*.3pm*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/FormValidator/
%{perl_vendorlib}/Data/FormValidator.pm

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 4.65-1
- Updated to version 4.65.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 4.63-1
- Updated to version 4.63.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 4.61-1
- Updated to release 4.61.

* Wed Nov 21 2007 Dag Wieers <dag@wieers.com> - 4.57-1
- Initial package. (using DAR)
