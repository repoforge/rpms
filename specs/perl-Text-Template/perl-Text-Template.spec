# $Id$
# Authority: dries
# Upstream: Mark Jason Dominus <mjd$plover,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Template

Summary: Text templates functions
Name: perl-Text-Template
Version: 1.45
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Template/

Source: http://www.cpan.org/modules/by-module/Text/Text-Template-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a library for generating form letters, building HTML pages, or
filling in templates generally.  A `template' is a piece of text that
has little Perl programs embedded in it here and there.  When you
`fill in' a template, you evaluate the little programs and replace
them with their values.

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
%doc Artistic COPYING INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/Text::Template.3pm*
%doc %{_mandir}/man3/Text::Template::*.3pm*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/Template/
%{perl_vendorlib}/Text/Template.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.45-1
- Updated to release 1.45.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.44-1
- Initial package.
