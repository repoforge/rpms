# $Id$
# Authority: dag
# Upstream: Ken MacLeod <ken$bitsko,slc,ut,us>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Grove

Summary: Perl module named XML-Grove
Name: perl-XML-Grove
Version: 0.05
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Grove/

Source: http://www.cpan.org/modules/by-module/XML/XML-Grove-%{version}alpha.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-XML-Grove is a Perl module.

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
%doc COPYING ChangeLog Changes MANIFEST README examples/
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Grove/
%{perl_vendorlib}/XML/Grove.pm
%dir %{perl_vendorlib}/XML/Parser/
%{perl_vendorlib}/XML/Parser/Grove.pm

%changelog
* Sat Oct 06 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
