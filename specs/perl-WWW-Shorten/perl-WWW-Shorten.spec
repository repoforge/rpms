# $Id$
# Authority: cmr
# Upstream: Iain Truskett <spoon$cpan,org>
# Upstream: Based on WWW::MakeAShorterLink by Dave Cross <dave$mag-sol,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Shorten

Summary: Interface to URL shortening sites
Name: perl-WWW-Shorten
Version: 2.04
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Shorten/

Source: http://cpan.cpantesters.org/authors/id/D/DA/DAVECROSS/WWW-Shorten-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.006
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More) >= 0.47
# From yaml requires
BuildRequires: perl(LWP) >= 5.75
BuildRequires: perl(LWP::UserAgent) >= 2.023
BuildRequires: perl(URI) >= 1.27
Requires: perl >= 0:5.006

Conflicts: shorten

%description
Interface to URL shortening sites.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS Artistic COPYING CREDITS ChangeLog.SPOON Changes INSTALL LICENCE MANIFEST MANIFEST.SKIP META.yml README TODO
%doc %{_mandir}/man3/WWW::Shorten*.3pm*
%doc %{_mandir}/man1/shorten.1*
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/Shorten/
%{perl_vendorlib}/WWW/Shorten.pm
%{_bindir}/shorten

%changelog
* Wed Nov 03 2010 Steve Huff <shuff@vecna.org> - 2.04-2
- File conflict (%{_bindir}/shorten) with shorten.

* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 2.04-1
- Updated to version 2.04.

* Thu Jun 11 2009 Unknown - 2.03-1
- Initial package. (using DAR)
