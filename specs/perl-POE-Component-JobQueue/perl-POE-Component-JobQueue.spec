# $Id$
# Authority: dag
# Upstream: Rocco Caputo <rcaputo@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-JobQueue

Summary: Handle large numbers of tasks with finite numbers of workers.
Name: perl-POE-Component-JobQueue
Version: 0.570
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-JobQueue/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-JobQueue-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(POE) >= 1.007


%description
Handle large numbers of tasks with finite numbers of workers..

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
%doc CHANGES MANIFEST META.yml README
%doc %{_mandir}/man3/POE::Component::JobQueue.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%{perl_vendorlib}/POE/Component/JobQueue.pm

%changelog
* Wed Aug  5 2009 Christoph Maser <cmr@financial.com> - 0.570-1
- Updated to version 0.570.

* Thu Jul 30 2009 Christoph Maser <cmr@financial.com> - 0.56-1
- Updated to version 0.56.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.55-1
- Initial package. (using DAR)
