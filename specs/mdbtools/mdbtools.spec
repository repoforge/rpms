# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Access data stored in Microsoft Access databases.
Name: mdbtools
Version: 0.5
Release: 0
License: LGPL/GPL
Group: System Environment/Libraries
URL: http://mdbtools.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/mdbtools/mdbtools-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: unixODBC-devel >= 2.0.0, libgnomeui-devel >= 2.0
 
%description 
MDB Tools is a suite of libraries and program for accessing data stored
in Microsoft Access databases.
 
%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package gui
Summary: gmdb2 graphical interface for MDB Tools.
Group: Applications/Databases
Requires: %{name} = %{version}-%{release}
 
%description gui
The mdbtools-gui package contains the gmdb2 graphical user interface
for MDB Tools

%prep
%setup 
 
%{__cat} <<EOF >gmdb2.desktop
[Desktop Entry]
Name=MDB database explorer
Comment=A graphical database explorer for MDB files.
Icon=gnome-day.png
Exec=gmdb2
Terminal=false
Type=Application
EOF

%build 
%configure \
	--with-unixodbc="%{_prefix}"
%{__make} %{?_smp_mflags}
 
%install 
%{__rm} -rf %{buildroot}
%makeinstall

%if %{dfi}
        %{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Development/
        %{__install} -m0644 gmdb2.desktop %{buildroot}%{_datadir}/gnome/apps/Development/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--add-category Application                 \
		--add-category Development                 \
		--dir %{buildroot}%{_datadir}/applications \
		gmdb2.desktop
%endif

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig 

%postun
/sbin/ldconfig 
 
%clean 
%{__rm} -rf %{buildroot}
 
%files 
%defattr(-, root, root, 0755) 
%doc AUTHORS ChangeLog COPYING* INSTALL NEWS README TODO
%doc doc/*.html doc/*.txt
%doc %{_mandir}/man?/*
%{_bindir}/mdb-*
%{_bindir}/pr*
%{_bindir}/unittest
%{_bindir}/updrow
%{_libdir}/*.so.*
 
%files devel 
%defattr (-, root, root, 0755) 
%doc HACKING
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h

%files gui
%defattr (-, root, root, 0755)
%doc %{_datadir}/gnome/help/gmdb/
%{_bindir}/gmdb2
%{_datadir}/gmdb/
%if %{dfi}
        %{_datadir}/gnome/apps/Development/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif
 
%changelog 
* Fri Jun 13 2003 Dag Wieers <dag@wieers.com> - 0.5-0
- Initial package. (using DAR)
