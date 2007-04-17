# $Id$
# Authority: dries
# Upstream: Mattias Hultgren <konst$matildahultgren,se>

Summary: Advanced calculator with support for matrices and graphs
Name: ump
Version: 0.8.6
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://u-m-p.sourceforge.net

Source: http://dl.sf.net/u-m-p/ump-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel, gcc-c++

%description
Ump is a program in which all sorts of calculations can be done, from the 
simplest to the more advanced. It handles complex numbers and matrices of 
those. The complex numbers are built up by either floating point values or 
ratios of arbitrary sized integers. Ump also draws graphs, ordinary, polar, 
and parameter, which is done through an easy to use user interface. It's also 
possible to write your own functions using the built in editor.

%prep
%setup

%build
#configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir}
%{__make} install DESTDIR="%{buildroot}" BIN_DIR=%{buildroot}%{_bindir} DATA_DIR=%{buildroot}%{_datadir}/ump

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog INSTALL LICENSE TODO
%{_bindir}/ump
%{_datadir}/ump/

%changelog
* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.6-1
- Initial package.
