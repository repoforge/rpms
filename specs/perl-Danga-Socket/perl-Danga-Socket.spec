# $Id$
# Authority: dag
# Upstream: Matt Sergeant <msergeant$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Danga-Socket

Summary: Perl module that implements an event loop and event-driven async socket base class
Name: perl-Danga-Socket
Version: 1.58
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Danga-Socket/

Source: http://www.cpan.org/modules/by-module/Danga/Danga-Socket-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Danga-Socket is a Perl module that implements an event loop and
event-driven async socket base class.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml examples/
%doc %{_mandir}/man3/Danga::Socket.3pm*
%dir %{perl_vendorlib}/Danga/
%{perl_vendorlib}/Danga/Socket.pm

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.58-1
- Updated to release 1.58.

* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 1.57-1
- Initial package. (using DAR)
