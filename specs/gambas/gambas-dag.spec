# Authority: dag
# Upstream: Benoît Minisini <gambas$users,sf,net>

Summary: BASIC compiler, IDE and GUI builder
Name: gambas
Version: 0.55
Release: 0%{?dist}
License: GPL
Group: Development/Tools
URL: http://gambas.sourceforge.net/

Source: http://gambas.sf.net/gambas-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: postgresql-devel, mysql-devel, qt-devel, qt2-devel

%description
Gambas is still in development, but already usefull for smaller projects.
The IDE itself is written in Gambas-BASIC. The source can be used reviewed as an example application in the /usr/share/doc/packages/gambas directory. Documentation is also in that directory.

%prep
%setup

%build
CXXFLAGS="%{optflags} -fpermissive -L/usr/lib/qt2/lib" \
%configure \
	--with-qt-libraries="/usr/lib/qt3/lib" \
	--with-qt-includes="/usr/lib/qt3/include" \
	--with-pgsql-libraries="/usr/lib" \
	--enable-optimization
%{__make} %{?_smp_mflags}

%install
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*.h

%changelog
* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 0.55-0
- Initial package. (using DAR)
