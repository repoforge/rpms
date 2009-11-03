# $Id$
# Authority: dag
# Upstream: Lars Dɪ<daxim$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Yahoo-Photos
%define real_version 0.000002

Summary: Perl module to manage Yahoo Photos
Name: perl-Yahoo-Photos
Version: 0.0.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Yahoo-Photos/

Source: http://www.cpan.org/modules/by-module/Yahoo/Yahoo-Photos-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::Spiffy)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(File::Temp)
BuildRequires: perl(HTTP::Cookies::Netscape)
BuildRequires: perl(List::Util)
BuildRequires: perl(Perl::Version)
BuildRequires: perl(Readonly)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More) >= 0.42
BuildRequires: perl(WWW::Mechanize)

%description
perl-Yahoo-Photos is a Perl module to manage Yahoo Photos.

This package contains the following Perl module:

    Yahoo::Photos

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man1/yahoo-photos.1*
%doc %{_mandir}/man3/Yahoo::Photos.3pm*
%doc %{_mandir}/man3/Yahoo::Photos::Album.3pm*
%{_bindir}/yahoo-photos
%dir %{perl_vendorlib}/Yahoo/
%{perl_vendorlib}/Yahoo/Photos/
%{perl_vendorlib}/Yahoo/Photos.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.0.2-1
- Initial package. (using DAR)
