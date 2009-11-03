# $Id$
# Authority: dag
# Upstream: Dave Brondsema <dave$brondsema,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-SpamAssassin-Plugin-OpenPGP
%define real_version 1.000004

Summary: SpamAssassin plugin that validates OpenPGP signed email
Name: perl-Mail-SpamAssassin-Plugin-OpenPGP
Version: 1.0.4
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-SpamAssassin-Plugin-OpenPGP/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-SpamAssassin-Plugin-OpenPGP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(Mail::GPG) >= 1.0.6
BuildRequires: perl(Mail::SpamAssassin) >= 3.001
BuildRequires: perl(Module::Build) >= 0.26
BuildRequires: perl(Test::More)

%description
A SpamAssassin plugin that validates OpenPGP signed email.

%prep
%setup -n %{real_name}-%{version}

%build
#%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
#%{__make} %{?_smp_mflags}
%{__perl} Build.PL
./Build

%install
%{__rm} -rf %{buildroot}
#%{__make} pure_install
PERL_INSTALL_ROOT="%{buildroot}" ./Build install installdirs="vendor"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE-Apache.txt MANIFEST MANIFEST.SKIP META.yml NOTICE.txt README SIGNATURE
%doc %{_mandir}/man3/Mail::SpamAssassin::Plugin::OpenPGP.3pm*
%dir %{perl_vendorlib}/Mail/
%dir %{perl_vendorlib}/Mail/SpamAssassin/
%dir %{perl_vendorlib}/Mail/SpamAssassin/Plugin/
#%{perl_vendorlib}/Mail/SpamAssassin/Plugin/OpenPGP/
%{perl_vendorlib}/Mail/SpamAssassin/Plugin/OpenPGP.pm

%changelog
* Sun Nov 09 2008 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Initial package. (using DAR)
