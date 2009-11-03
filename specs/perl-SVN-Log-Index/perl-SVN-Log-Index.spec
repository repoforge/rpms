# $Id$
# Authority: dries
# Upstream: Nik Clayton, <nikc$cpan,org>
# Upstream: Garrett Rooney <rooneg$electricjellyfish,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVN-Log-Index

Summary: Index and search over Subversion commit logs
Name: perl-SVN-Log-Index
Version: 0.51
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Log-Index/

Source: http://www.cpan.org/modules/by-module/SVN/SVN-Log-Index-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: subversion-perl
BuildRequires: perl-Module-Build

%description
SVN::Log::Index builds a Plucene index of commit logs from any number of
Subversion repositories and allows you to do arbitrary full text
searches over them.

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
%doc CHANGES MANIFEST MANIFEST.SKIP META.yml README SIGNATURE TODO
%doc %{_mandir}/man1/sli.1*
%doc %{_mandir}/man3/SVN::Log::Index.3pm*
%{_bindir}/sli
%dir %{perl_vendorlib}/SVN/
%dir %{perl_vendorlib}/SVN/Log/
#%{perl_vendorlib}/SVN/Log/Index/
%{perl_vendorlib}/SVN/Log/Index.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.51-1
- Updated to release 0.51.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.41-1
- Updated to release 0.41.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Initial package.
