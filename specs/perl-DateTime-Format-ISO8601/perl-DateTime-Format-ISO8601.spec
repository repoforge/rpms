# $Id$
# Authority: dries
# Upstream: Joshua Hoblitt <jhoblitt$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-ISO8601

Summary: Parses ISO8601 formats
Name: perl-DateTime-Format-ISO8601
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-ISO8601/

Source: http://search.cpan.org/CPAN/authors/id/J/JH/JHOBLITT/DateTime-Format-ISO8601-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)
BuildRequires: perl(DateTime) >= 0.18
BuildRequires: perl(DateTime::Format::Builder) >= 0.77
Requires: perl(DateTime) >= 0.18
Requires: perl(DateTime::Format::Builder) >= 0.77


%description
Parses ISO8601 formats.

This package contains the following Perl module:

    DateTime::Format::ISO8601

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README Todo
%doc %{_mandir}/man3/DateTime::Format::ISO8601.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Format/
%{perl_vendorlib}/DateTime/Format/ISO8601.pm
%{perl_vendorlib}/DateTime/Format/ISO8601.pod

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.07-1
- Updated to version 0.07.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Updated to release 0.06.

* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.0403-1
- Initial package.
