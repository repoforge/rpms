# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-Builder

Summary: Create DateTime parser classes and objects
Name: perl-DateTime-Format-Builder
Version: 0.7901
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-Builder/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-Builder-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
With this module, you can create DateTime parser classes and objects.

This package contains the following Perl module:

    DateTime::Format::Builder

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Artistic COPYING CREDITS Changes INSTALL LICENCE MANIFEST MANIFEST.SKIP META.yml README SIGNATURE examples/
%doc %{_mandir}/man3/DateTime::Format::Builder.3pm*
%doc %{_mandir}/man3/DateTime::Format::Builder::*.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Format/
%{perl_vendorlib}/DateTime/Format/Builder/
%{perl_vendorlib}/DateTime/Format/Builder.pm
%{perl_vendorlib}/DateTime/Format/Builder.pod

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.7901-1
- Updated to release 0.7901.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.7807-1
- Updated to release 0.7807.

* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.7806-1
- Initial package.
