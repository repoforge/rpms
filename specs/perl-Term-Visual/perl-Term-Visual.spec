# $Id$
# Authority: dag
# Upstream: Charles Ayres <lunartear$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Term-Visual

Summary: Curses split-terminal interface for applications
Name: perl-Term-Visual
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-Visual/

Source: http://www.cpan.org/modules/by-module/Term/Term-Visual-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Curses split-terminal interface for applications.

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
%doc INSTALL MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Term::Visual.3pm*
%dir %{perl_vendorlib}/Term/
%{perl_vendorlib}/Term/Visual/
%{perl_vendorlib}/Term/Visual.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
