# $Id$
# Authority: dag

%define perlvendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)

Summary: Project Builder helps providing multi-OSes Continuous Packaging
Name: project-builder
Version: 0.9.10
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://trac.project-builder.org

Source: ftp://ftp.project-builder.org/src/project-builder-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: perl >= 5.8.4
Requires: perl-DateManip
Requires: perl-ProjectBuilder
Requires: rpm-build

%description
ProjectBuilder aka pb helps producing packages
for multiple OSes (Linux distributions, Solaris, ...).
It does that by minimizing
the duplication of information required and
a set a very simple configuration files.
It implements a Continuous Packaging approach.

%prep
%setup

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;
find %{buildroot} -name perllocal.pod -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README
%doc %{_mandir}/man1/pb.1*
%doc %{_mandir}/man3/ProjectBuilder::*.3pm*
%{_bindir}/pb
%{_bindir}/pbg
%{_bindir}/pbvi
%{perl_vendorlib}/ProjectBuilder/

%changelog
* Tue Jun 08 2010 Dag Wieers <dag@wieers.com> - 0.9.10-1
- Initial package. (using DAR)
