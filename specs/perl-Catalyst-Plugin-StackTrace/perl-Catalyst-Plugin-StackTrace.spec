# $Id$
# Authority: dag
# Upstream: Andy Grundman, <andy$hybridized,org>
# Upstream: Matt S, Trout, <mst$shadowcatsystems,co,uk>
# ExcludeDist: el4  <- inherited by Catalyst::Runtime


%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-StackTrace

Summary: Display a stack trace on the debug screen
Name: perl-Catalyst-Plugin-StackTrace
Version: 0.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-StackTrace/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSTROUT/Catalyst-Plugin-StackTrace-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst) >= 5.70
BuildRequires: perl(Devel::StackTrace)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(MRO::Compat) >= 0.10
BuildRequires: perl >= 5.8.1
Requires: perl(Catalyst) >= 5.70
Requires: perl(Devel::StackTrace)
Requires: perl(MRO::Compat) >= 0.10
Requires: perl >= 5.8.1

%filter_from_requires /^perl*/d
%filter_setup


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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Catalyst::Plugin::StackTrace.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
#%{perl_vendorlib}/Catalyst/Plugin/StackTrace/
%{perl_vendorlib}/Catalyst/Plugin/StackTrace.pm

%changelog
* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
