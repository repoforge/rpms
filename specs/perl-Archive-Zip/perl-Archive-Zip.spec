# Authority: dag

%define rname Archive-Zip

Summary: Archive-Zip module for perl
Name: perl-Archive-Zip
Version: 1.05
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Archive-Zip/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/authors/id/N/NE/NEDKONZ/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl(Compress::Zlib) >= 1.08
Requires: perl >= 0:5.00503, perl(Compress::Zlib) >= 1.08

%description
The Archive::Zip module allows a Perl program to create, manipulate,
read, and write Zip archive files.

Zip archives can be created, or you can read from existing zip files.
Once created, they can be written to files, streams, or strings.

%prep
%setup -n %{rname}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README TODO docs/* examples
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/perl5/

%changelog
* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 1.05-0
- Initial package. (using DAR)
