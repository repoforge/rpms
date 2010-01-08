# $Id$
# Authority: dag
# Upstream: Matt S Trout <perl-stuff@trout.me.uk>
# ExcludeDist: el4  <- inherited by Catalyst::Runtime

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Session-Store-FastMmap

Summary: FastMmap session storage backend
Name: perl-Catalyst-Plugin-Session-Store-FastMmap
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Session-Store-FastMmap/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSTROUT/Catalyst-Plugin-Session-Store-FastMmap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Cache::FastMmap) >= 1.29
BuildRequires: perl(Catalyst::Plugin::Session) >= 0.27
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Path::Class)
Requires: perl(Cache::FastMmap) >= 1.29
Requires: perl(Catalyst::Plugin::Session) >= 0.27
Requires: perl(File::Spec)
Requires: perl(File::Temp)
Requires: perl(MRO::Compat)
Requires: perl(Path::Class)

%filter_from_requires /^perl*/d
%filter_setup


%description
FastMmap session storage backend.

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
%doc %{_mandir}/man3/Catalyst::Plugin::Session::Store::FastMmap.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/Session/
%dir %{perl_vendorlib}/Catalyst/Plugin/Session/Store/
#%{perl_vendorlib}/Catalyst/Plugin/Session/Store/FastMmap/
%{perl_vendorlib}/Catalyst/Plugin/Session/Store/FastMmap.pm

%changelog
* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 0.13-1
- Updated to version 0.13.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
