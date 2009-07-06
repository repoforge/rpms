# $Id$
# Authority: matthias
# Upstream: Jörn Reder <joern$zyn,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Event-RPC

Summary: Event based transparent Client/Server RPC framework
Name: perl-Event-RPC
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Event-RPC/

Source: http://www.cpan.org/modules/by-module/Event/Event-RPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Event)
# Provided by either perl or perl-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::Socket::SSL)
Requires: perl(IO::Socket::SSL)

%description
Event based transparent Client/Server RPC framework.

%prep
%setup -n %{real_name}-%{version}
# Make it so that the .pl scripts in %%doc don't add bogus requirements
%{__chmod} -x examples/*.pl

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
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Event::RPC.3pm*
%doc %{_mandir}/man3/Event::RPC::*.3pm*
%dir %{perl_vendorlib}/Event/
%{perl_vendorlib}/Event/RPC/
%{perl_vendorlib}/Event/RPC.pm

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 1.01-1
- Updated to version 1.01.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.00-1
- Updated to release 1.00.

* Thu May 31 2007 Matthias Saou <http://freshrpms.net/> 0.90-2
- Build require perl(ExtUtils::MakeMaker) for F7.

* Thu Jun  1 2006 Dries Verachtert <dries@ulyssis.org> - 0.90-1
- Updated to release 0.90.

* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 0.89-1
- Update to 0.89.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.88-2
- Release bump to drop the disttag number in FC5 build.

* Mon Jan  9 2006 Matthias Saou <http://freshrpms.net/> 0.88-1
- Initial RPM package.

