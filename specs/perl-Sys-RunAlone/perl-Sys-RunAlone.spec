# $Id$
# Authority: dries
# Upstream: Elizabeth Mattijsen <liz$dijkmat,nl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-RunAlone

Summary: Run only one invocation
Name: perl-Sys-RunAlone
Version: 0.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-RunAlone/

Source: http://www.cpan.org/modules/by-module/Sys/Sys-RunAlone-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Make sure only one invocation of a script is active at a time.

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
%doc CHANGELOG MANIFEST META.yml README
%doc %{_mandir}/man3/Sys::RunAlone.3pm*
%dir %{perl_vendorlib}/Sys/
#%{perl_vendorlib}/Sys/RunAlone/
%{perl_vendorlib}/Sys/RunAlone.pm

%changelog
* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 0.09-1
- Updated to version 0.09.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Thu Jan 04 2007 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
