# $Id$
# Authority: dag

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Archive-Zip

Summary: Archive-Zip module for perl
Name: perl-Archive-Zip
Version: 1.09
Release: 0
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Archive-Zip/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/authors/id/N/NE/NEDKONZ/Archive-Zip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl(Compress::Zlib) >= 1.08
Requires: perl >= 0:5.00503, perl(Compress::Zlib) >= 1.08

%description
The Archive::Zip module allows a Perl program to create, manipulate,
read, and write Zip archive files.

Zip archives can be created, or you can read from existing zip files.
Once created, they can be written to files, streams, or strings.


%prep
%setup -n %{real_name}-%{version} 


%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

### FIXME: Change to real perl location. (Please fix upstream)
%{__perl} -pi -e 's|^#!/.*bin/perl|#!%{__perl}|i;' examples/*.pl

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}


%clean 
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc README TODO docs/* examples/
%doc %{_mandir}/man?/*
%{_bindir}/*
%{perl_vendorlib}/*


%changelog
* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.09-0
- Updated to release 1.09.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 1.05-0
- Initial package. (using DAR)
