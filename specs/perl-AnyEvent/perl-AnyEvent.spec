# $Id$
# Authority: matthias

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AnyEvent

Summary: Framework for multiple event loops
Name: perl-AnyEvent
Version: 1.02
Release: 1
License: Artistic or GPL
Group: Development/Libraries
URL: http://search.cpan.org/~mlehmann/AnyEvent/
Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/AnyEvent-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
#BuildRequires: perl(Coro), perl(Event), perl(Glib), perl(Tk)
BuildRequires: perl(Event), perl(Glib), perl(Tk)

%description
AnyEvent provides a framework for multiple event loops.


%prep
%setup -n %{real_name}-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod \
           %{buildroot}%{perl_vendorarch}/auto/*/.packlist


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc Changes COPYING README
%{perl_vendorlib}/AnyEvent/
%{perl_vendorlib}/AnyEvent.pm
%{_mandir}/man3/*


%changelog
* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 1.02-1
- Initial RPM release.

