# $Id: _template.spec 471 2004-05-03 19:42:19Z dag $
# Authority: dag
# Upstream: <morin$cs,carleton,ca>

%define real_version 6.0pre14

Summary: Extensible drawing editor
Name: ipe
Version: 6.0
Release: 0.pre14
License: GPL
Group: Publishing
URL: http://ipe.compgeom.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ipe.compgeom.org/ipe-%{real_version}-src.tar.gz
#Patch: http://cg.scs.carleton.ca/~morin/misc/ipe/ipe-6.0pre13-usr.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Ipe is a drawing editor for creating figures in PDF or (encapsulated)
Postscript format. It supports making small figures for inclusion into
LaTeX-documents as well as making multi-page PDF presentations that
can be shown on-line with Acrobat Reader. 

%prep
%setup -n %{name}-%{real_version}
#%patch -p1 -b.orig

%build
source /etc/profile.d/qt.sh
cd src
qmake main.pro
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall -C src

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_libdir}/*.so.*
%exclude %{_libdir}/*.so
%{_libdir}/ipe/

%changelog
* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 6.0-1
- Initial package. (using DAR)
