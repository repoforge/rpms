# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name FileHandle-Unget

Summary: FileHandle which supports multi-byte unget
Name: perl-FileHandle-Unget
Version: 0.1621
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/FileHandle-Unget/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/modules/by-module/FileHandle/FileHandle-Unget-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl(Test::More), perl(File::Spec::Functions)
BuildRequires: perl(ExtUtils::MakeMaker::bytes), perl(Scalar::Util) >= 1.14
Requires: perl >= 0:5.00503

%description
FileHandle::Unget implements a filehandle which supports multi-byte unget.

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
%doc CHANGES LICENSE MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/FileHandle/

%changelog
* Mon Feb 21 2005 Dag Wieers <dag@wieers.com> - 0.1621-1
- Initial package. (using DAR)
