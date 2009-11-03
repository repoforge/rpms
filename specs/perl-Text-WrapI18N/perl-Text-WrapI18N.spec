# $Id$
# Authority: dag
# Upstream: ??? ?? <kubota$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-WrapI18N

Summary: Perl module that implements line wrapping
Name: perl-Text-WrapI18N
Version: 0.06
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-WrapI18N/

Source: http://www.cpan.org/modules/by-module/Text/Text-WrapI18N-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Text-WrapI18N is a Perl module that implements line wrapping with
support for multibyte, fullwidth, and combining characters and
languages without whitespaces between words.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Text::WrapI18N.3pm*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/WrapI18N.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
