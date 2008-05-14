# $Id$
# Authority: dag
# Upstream: Niek Albers <nieka$daansystems,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-RPC

Summary: Pure Perl implementation for an XML-RPC client and server
Name: perl-XML-RPC
Version: 0.8
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-RPC/

Source: http://www.cpan.org/modules/by-module/XML/XML-RPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Pure Perl implementation for an XML-RPC client and server.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/XML::RPC.3pm*
%dir %{perl_vendorlib}/XML/
#%{perl_vendorlib}/XML/RPC/
%{perl_vendorlib}/XML/RPC.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 0.7-1
- Updated to release 0.7.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
