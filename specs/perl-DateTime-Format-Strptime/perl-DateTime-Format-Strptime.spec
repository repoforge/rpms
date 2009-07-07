# $Id$
# Authority: dries
# Upstream: Rick Measham <rickm$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-Strptime

Summary: Parse and format strp and strf time patterns
Name: perl-DateTime-Format-Strptime
Version: 1.0901
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-Strptime/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-Strptime-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module replicates most of Strptime for DateTime. Strptime is the
unix command that is the reverse of Strftime. While Strftime takes a
DateTime and outputs it in a given format, Strptime takes a DateTime and
a format and returns the DateTime object associated.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/DateTime::Format::Strptime.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Format/
#%{perl_vendorlib}/DateTime/Format/Strptime/
%{perl_vendorlib}/DateTime/Format/Strptime.pm

%changelog
* Tue Jul  7 2009 Christoph Maser <cmr@financial.com> - 1.0901-1
- Updated to version 1.0901.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.0800-1
- Updated to release 1.0800.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 1.0702-1
- Updated to release 1.0702.

* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 1.0700-1
- Initial package.
