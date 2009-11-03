# $Id$
# Authority: dag
# Upstream: Matthew C. Newton <perl03$takethisout,newtoncomputing,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PostScript-Simple

Summary: Perl module to produce PostScript files
Name: perl-PostScript-Simple
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PostScript-Simple/

Source: http://www.cpan.org/modules/by-module/PostScript/PostScript-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-PostScript-Simple is a Perl module to produce PostScript files.

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
%doc Changes MANIFEST META.yml README TODO examples/
%doc %{_mandir}/man3/PostScript::Simple.3pm*
%doc %{_mandir}/man3/PostScript::Simple::EPS.3pm*
%dir %{perl_vendorlib}/PostScript/
%{perl_vendorlib}/PostScript/Simple/
%{perl_vendorlib}/PostScript/Simple.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Initial package. (using DAR)
