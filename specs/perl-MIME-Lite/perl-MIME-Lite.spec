# $Id$
# Authority: dries

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-Lite

Summary: Simple standalone module for generating MIME messages
Name: perl-MIME-Lite
Version: 2.117
Release: 2
License: GPL
Group: Applications/CPAN
URL: http://www.zeegee.com/code/perl/MIME-Lite/

Source: http://www.zeegee.com/code/perl/MIME-Lite/download/MIME-Lite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
MIME-Lite is a simple standalone module for generating MIME messages.

%description -l nl
MIME-Lite is een eenvoudige onafhankelijke module om MIME berichten te
genereren.

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
%doc COPYING INSTALLING README*
%doc %{_mandir}/man3/MIME::Lite.3pm.gz
%{perl_vendorlib}/MIME/Lite.pm

%changelog
* Sun Dec 11 2004 Dries Verachtert <dries@ulyssis.org> 2.117-2
- cleanup of spec file

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 2.117-1
- first packaging for Fedora Core 1
