# $Id$

# Authority: dries

Summary: Implementation of XML-RPC in perl
Summary(nl): Een implementatie van XML-RPC in perl.
Name: perl-XML-RPC
Version: 0.53
Release: 2
License: GPL
Group: Applications/CPAN
URL: http://www.blackperl.com/RPC::XML/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJRAY/RPC-XML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl
Requires: perl

%description
perl-XML-RPC is an implementation of the XML-RPC standard in Perl. The goal
is to provide a client, a stand-alone server and an Apache/mod_perl
content-handler class.

%description -l nl
perl-XML-RPC is een implementatie van de XML-RPC standaard in Perl. Het doel
is het maken van een client, een onafhankelijke server een Apache/mod_perl
content-handler class.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup -n RPC-XML-0.53

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor"
sed -i "s/DESTDIR =.*/DESTDIR=${RPM_BUILD_ROOT//\//\\/}\//g;" Makefile
%{__make} %{?_smp_mflags}

%install
export DESTDIR=$RPM_BUILD_ROOT
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README 
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Sun Dec 11 2004 Dries Verachtert <dries@ulyssis.org> 0.53-2
- cleanup of spec file

* Fri Dec 26 2003 Dries Verachtert <dries@ulyssis.org> 0.53-1
- first packaging for Fedora Core 1
