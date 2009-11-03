# $Id$
# Authority: dries
# Upstream: Darren Chamberlain <darren$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Plugin-Number-Format

Summary: Plugin/filter interface to Number::Format
Name: perl-Template-Plugin-Number-Format
Version: 1.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Plugin-Number-Format/

Source: http://www.cpan.org/modules/by-module/Template/Template-Plugin-Number-Format-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Plugin/filter interface to Number::Format.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST META.yml
%doc %{_mandir}/man3/Template::Plugin::Number::Format.3pm*
%dir %{perl_vendorlib}/Template/
%dir %{perl_vendorlib}/Template/Plugin/
%dir %{perl_vendorlib}/Template/Plugin/Number/
%{perl_vendorlib}/Template/Plugin/Number/Format.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Thu Nov 10 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
