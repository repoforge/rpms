# $Id$
# Authority: cmr
# Upstream: Randy W, Sims <randys$thepierianspring,org>
# Upstream: Based partly on code from the Module::Build project
# by Ken Williams <kwilliams$cpan,org> and others,

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Probe-Perl

Summary: Information about the currently running perl
Name: perl-Probe-Perl
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Probe-Perl/

Source: http://www.cpan.org/authors/id/K/KW/KWILLIAMS/Probe-Perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(Test)
# From yaml requires
Requires: perl(Config)

%description
Information about the currently running perl.

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
%doc %{_mandir}/man3/Probe::Perl.3pm*
%dir %{perl_vendorlib}/Probe/
#%{perl_vendorlib}/Probe/Perl/
%{perl_vendorlib}/Probe/Perl.pm

%changelog
* Tue Sep 15 2009 Christoph Maser <cmr@financial.com> - 0.01-1
- Initial package. (using DAR)
