# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name MailTools

Summary: MailTools module for perl 
Name: perl-MailTools
Version: 1.66
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MailTools/

Source: http://www.cpan.org/modules/by-module/Mail/MailTools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: perl-Mail

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
%{?rh7:BuildRequires: perl-libnet >= 1.05}
Requires: perl >= 0:5.00503
%{?rh7:BuildRequires: perl-libnet >= 1.05}

%description
MailTools module for perl

%prep
%setup -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README*
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Mail/
%{perl_vendorlib}/auto/Mail/

%changelog
* Mon Feb 21 2005 Dag Wieers <dag@wieers.coM> - 1.66-1
- Updated to release 1.66.

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 1.64-0
- Updated to release 1.64.

* Fri Nov 28 2003 Dag Wieers <dag@wieers.com> - 1.60-0
- Updated to release 1.60.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.58-0
- Updated to release 1.58.

* Sun Jan 23 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
