# $Id$
# Authority: dag
# Upstream: Andy Grundman, <andy$hybridized,org>
# Upstream: Matt S, Trout, <mst$shadowcatsystems,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-StackTrace

Summary: Display a stack trace on the debug screen
Name: perl-Catalyst-Plugin-StackTrace
Version: 0.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-StackTrace/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-StackTrace-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst::Runtime)

%description
Display a stack trace on the debug screen.

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
%doc %{_mandir}/man3/Catalyst::Plugin::StackTrace.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
#%{perl_vendorlib}/Catalyst/Plugin/StackTrace/
%{perl_vendorlib}/Catalyst/Plugin/StackTrace.pm

%changelog
* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
