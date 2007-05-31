# $Id$
# Authority: matthias
# Upstream: Jörn Reder <joern$zyn,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Event-RPC

Summary: Event based transparent Client/Server RPC framework
Name: perl-Event-RPC
Version: 0.90
Release: 2
License: Artistic/GPL
Group: Development/Libraries
URL: http://search.cpan.org/dist/Event-RPC/
Source: http://search.cpan.org/CPAN/authors/id/J/JR/JRED/Event-RPC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: perl(IO::Socket::SSL)
BuildRequires: perl(Event), perl(IO::Socket::SSL)
# Provided by either perl or perl-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildArch: noarch

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
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod \
           %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc Changes examples/ README
%dir %{perl_vendorlib}/Event/
%{perl_vendorlib}/Event/RPC/
%{perl_vendorlib}/Event/RPC.pm
%{_mandir}/man3/*


%changelog
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

