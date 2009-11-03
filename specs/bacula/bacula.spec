# Platform Build Configuration

# basic defines for every build
%define depkgs ../depkgs
%define depkgs_version 24Jul03
%define tomsrtbt tomsrtbt-2.0.103
%define sqlite_bindir /usr/lib/sqlite
%define working_dir /var/bacula

# platform defines - set one below or define the build_xxx on the command line
# RedHat builds
%define rh7 0
%{?build_rh7:%define rh7 1}
%define rh8 0
%{?build_rh8:%define rh8 1}
%define rh9 0
%{?build_rh9:%define rh9 1}
# Fedora Core 1 build
%define fc1 0
%{?build_fc1:%define fc1 1}
# Whitebox Enterprise build
%define wb3 0
%{?build_wb3:%define wb3 1}
# SuSE 9.0 build
%define su9 0
%{?build_su9:%define su9 1}

# database defines
# set for database support desired
%define mysql 0
%{?build_mysql:%define mysql 1}
%define sqlite 0
%{?build_sqlite:%define sqlite 1}

Summary: Network backup solution
Name: bacula
Version: 1.32
Release: 1.f%{?dist}
License: GPL v2
Group: System Environment/Daemons
URL: http://www.bacula.org/

Source: http://dl.sf.net/bacula/bacula-%{version}.tar.gz
Source1: http://dl.sf.net/bacula/depkgs-%{depkgs_version}.tar.gz
Source2: http://www.tux.org/pub/distributions/tinylinux/tomsrtbt/%{tomsrtbt}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: readline-devel, atk-devel, ncurses-devel, pango-devel
BuildRequires: libstdc++-devel, libxml2-devel, zlib-devel
%if %{rh7}
BuildRequires: libtermcap-devel
BuildRequires: gtk+-devel >= 1.2
BuildRequires: gnome-libs-devel >= 1.4
BuildRequires: glibc-devel >= 2.2
BuildRequires: ORBit-devel
BuildRequires: bonobo-devel
BuildRequires: GConf-devel
%endif
%if ! %{rh7} && ! %{su9}
BuildRequires: libtermcap-devel
BuildRequires: gtk2-devel >= 2.0
BuildRequires: libgnomeui-devel >= 2.0
BuildRequires: glibc-devel >= 2.3
BuildRequires: ORBit2-devel
BuildRequires: libart_lgpl-devel >= 2.0
BuildRequires: libbonobo-devel >= 2.0
BuildRequires: libbonoboui-devel >= 2.0
BuildRequires: bonobo-activation-devel
BuildRequires: GConf2-devel
BuildRequires: linc-devel
%endif

%if %{mysql}
BuildRequires: mysql-devel >= 3.23
%endif

%description
Bacula - It comes by night and sucks the vital essence from your computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.
Bacula source code has been released under the GPL version 2 license.

%if %{mysql}
%package mysql
%endif
%if %{sqlite}
%package sqlite
%endif

Summary: Bacula - The Network Backup Solution
Group: System Environment/Daemons
Provides: bacula-dir, bacula-sd, bacula-fd, bacula-server
Conflicts: bacula-client, bacula-gconsole
Requires: readline, perl, atk, ncurses, pango, libstdc++
Requires: libxml2, zlib
%if %{rh7}
Requires: gtk+ >= 1.2
Requires: gnome-libs >= 1.4
Requires: glibc >= 2.2
Requires: ORBit
Requires: bonobo
Requires: GConf
Requires: libtermcap
%endif
%if ! %{rh7} && ! %{su9}
Requires: gtk2 >= 2.0
Requires: libgnomeui >= 2.0
Requires: glibc >= 2.3
Requires: ORBit2
Requires: libart_lgpl >= 2.0
Requires: libbonobo >= 2.0
Requires: libbonoboui >= 2.0
Requires: bonobo-activation
Requires: GConf2
Requires: linc
Requires: libtermcap
%endif
%if %{mysql} && ! %{su9}
Requires: mysql >= 3.23
Requires: mysql-server >= 3.23
%endif
%if %{mysql} && %{su9}
Requires: mysql >= 3.23
Requires: mysql-client >= 3.23
%endif

%if %{mysql}
%description mysql
%endif
%if %{sqlite}
%description sqlite
%endif

Bacula - It comes by night and sucks the vital essence from your computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.
Bacula source code has been released under the GPL version 2 license.

%if %{mysql}
This build requires MySQL to be installed separately as the catalog database.
%endif
%if %{sqlite}
This build incorporates sqlite as the catalog database, statically compiled.
%endif

%package client
Summary: Bacula - The Network Backup Solution
Group: System Environment/Daemons
Provides: bacula-fd
Requires: readline, perl, libstdc++, zlib

%if %{rh7}
Requires: glibc >= 2.2
Requires: libtermcap
%endif
%if ! %{rh7} && ! %{su9}
Requires: glibc >= 2.3
Requires: libtermcap
%endif

%description client
Bacula - It comes by night and sucks the vital essence from your computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.
Bacula source code has been released under the GPL version 2 license.

This is the File daemon (Client) only package. It includes the command line
console program.

%package rescue

Summary: Bacula - The Network Backup Solution
Group: System Environment/Daemons
Requires: coreutils, util-linux, libc5, bacula-fd

%description rescue
Bacula - It comes by night and sucks the vital essence from your computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.
Bacula source code has been released under the GPL version 2 license.

This package installs scripts for disaster recovery and builds rescue
floppy disks for bare metal recovery. This package includes tomsrtbt
(http://www.toms.net/rb/, by Tom Oehser, Tom@Toms.NET) to provide a tool
to build a boot floppy disk.

You need to have the bacula-sqlite, bacula-mysql, bacula-postgresql or
bacula-client package for your platform installed and configured before
installing this package.

To create a boot disk run "./getdiskinfo" from the /etc/bacula/rescue
directory (this is done when the package is first installed),
then run "./install.s" from the /etc/bacula/rescue/tomsrtbt/
directory. To make the bacula rescue disk run
"./make_rescue_disk --copy-static-bacula --copy-etc-files"
from the /etc/bacula/rescue directory. To recreate the rescue
information for this system run ./getdiskinfo again.

%package gconsole
Summary: Bacula - The Network Backup Solution
Group: System Environment/Daemons
Requires: readline, libstdc++, zlib, pango, bacula-client
Conflicts: bacula-server

%if %{rh7}
Requires: gtk+ >= 1.2
Requires: gnome-libs >= 1.4
Requires: glibc >= 2.2
Requires: ORBit
Requires: bonobo
Requires: GConf
%endif

%description gconsole
Bacula - It comes by night and sucks the vital essence from your computers.

Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.
Bacula source code has been released under the GPL version 2 license.

This is the Gnome Console package. It is an add-on to the client package.

%prep
%setup -b 1
%setup -b 2

%build
cwd=${PWD}
cd %{depkgs}
%if %{sqlite}
make sqlite
%endif
make mtx
cd ${cwd}

# patches for the bundled sqlite scripts

# patch the make_sqlite_tables script for installation bindir
patch src/cats/make_sqlite_tables.in src/cats/make_sqlite_tables.in.patch

# patch the create_sqlite_database script for installation bindir
patch src/cats/create_sqlite_database.in src/cats/create_sqlite_database.in.patch

# patch the make_catalog_backup script for installation bindir
patch src/cats/make_catalog_backup.in src/cats/make_catalog_backup.in.patch

# patch the update_sqlite_tables script for installation bindir
patch src/cats/update_sqlite_tables.in src/cats/update_sqlite_tables.in.patch

%configure \
        --sysconfdir="/etc/bacula" \
        --with-scriptdir="/etc/bacula" \
        --enable-smartalloc \
        --enable-gnome \
	--enable-static-fd \
%{?mysql:--with-mysql} \
%{?sqlite:--with-sqlite="${cwd}/../depkgs/sqlite"} \
        --with-working-dir="%{working_dir}" \
        --with-pid-dir="/var/run" \
        --with-subsys-dir="/var/lock/subsys"
%{__make} %{?_smp_mflags}

cd src/filed
strip static-bacula-fd
cd ../../

%install
%{__rm} -rf %{buildroot}
cwd=${PWD}
mkdir -p $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps
mkdir -p $RPM_BUILD_ROOT/usr/share/gnome/apps/System
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
mkdir -p $RPM_BUILD_ROOT/etc/bacula/rescue
mkdir -p $RPM_BUILD_ROOT/etc/bacula/rescue/tomsrtbt

%if %{sqlite}
mkdir -p $RPM_BUILD_ROOT%{sqlite_bindir}
%endif

make \
        prefix=$RPM_BUILD_ROOT/usr \
        sbindir=$RPM_BUILD_ROOT/usr/sbin \
        sysconfdir=$RPM_BUILD_ROOT/etc/bacula \
        scriptdir=$RPM_BUILD_ROOT/etc/bacula \
        working_dir=$RPM_BUILD_ROOT%{working_dir} \
        install

%{__make} -C %{depkgs} \
        prefix="$RPM_BUILD_ROOT/usr" \
        sbindir="$RPM_BUILD_ROOT/usr/sbin" \
        sysconfdir="$RPM_BUILD_ROOT/etc/bacula" \
        working_dir="$RPM_BUILD_ROOT%{working_dir}" \
        mandir="$RPM_BUILD_ROOT/usr/man" \
        mtx-install

# fixme - make installs the mysql scripts for sqlite build
%if %{sqlite}
rm -f $RPM_BUILD_ROOT/etc/bacula/startmysql
rm -f $RPM_BUILD_ROOT/etc/bacula/stopmysql
rm -f $RPM_BUILD_ROOT/etc/bacula/grant_mysql_privileges
%endif

cp -p platforms/redhat/bacula-dir $RPM_BUILD_ROOT/etc/init.d/bacula-dir
cp -p platforms/redhat/bacula-fd $RPM_BUILD_ROOT/etc/init.d/bacula-fd
cp -p platforms/redhat/bacula-sd $RPM_BUILD_ROOT/etc/init.d/bacula-sd
chmod 0754 $RPM_BUILD_ROOT/etc/init.d/*

# install the menu stuff
cp -p scripts/bacula.png $RPM_BUILD_ROOT/usr/share/pixmaps/bacula.png
cp -p scripts/bacula.desktop.gnome1 $RPM_BUILD_ROOT/usr/share/gnome/apps/System/bacula.desktop
cp -p scripts/bacula.desktop.gnome2 $RPM_BUILD_ROOT/usr/share/applications/bacula.desktop

# install sqlite
%if %{sqlite}
cp -p ../depkgs/sqlite/sqlite $RPM_BUILD_ROOT%{sqlite_bindir}/sqlite
cp -p ../depkgs/sqlite/sqlite.h $RPM_BUILD_ROOT%{sqlite_bindir}/sqlite.h
cp -p ../depkgs/sqlite/libsqlite.a $RPM_BUILD_ROOT%{sqlite_bindir}/libsqlite.a
%endif

# install the logrotate file
cp -p scripts/logrotate $RPM_BUILD_ROOT/etc/logrotate.d/bacula

# install the rescue stuff
# these are the rescue scripts
cp -p rescue/linux/backup.etc.list $RPM_BUILD_ROOT/etc/bacula/rescue/
cp -p rescue/linux/format_floppy $RPM_BUILD_ROOT/etc/bacula/rescue/
cp -p rescue/linux/getdiskinfo $RPM_BUILD_ROOT/etc/bacula/rescue/
cp -p rescue/linux/make_rescue_disk $RPM_BUILD_ROOT/etc/bacula/rescue/
cp -p rescue/linux/restore_bacula $RPM_BUILD_ROOT/etc/bacula/rescue/
cp -p rescue/linux/restore_etc $RPM_BUILD_ROOT/etc/bacula/rescue/
cp -p rescue/linux/run_grub $RPM_BUILD_ROOT/etc/bacula/rescue/
cp -p rescue/linux/run_lilo $RPM_BUILD_ROOT/etc/bacula/rescue/
cp -p rescue/linux/sfdisk.bz2 $RPM_BUILD_ROOT/etc/bacula/rescue/

# this is the static file daemon
cp -p src/filed/static-bacula-fd $RPM_BUILD_ROOT/etc/bacula/rescue/bacula-fd

# this is the tom's root boot disk
cp -p ../%{tomsrtbt}/* $RPM_BUILD_ROOT/etc/bacula/rescue/tomsrtbt/

# now clean up permissions that are left broken by the install
chmod o-r $RPM_BUILD_ROOT/etc/bacula/query.sql
chmod o-rwx $RPM_BUILD_ROOT/var/bacula

%clean
%{__rm} -rf %{buildroot}

%if %{mysql}

%files mysql
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog INSTALL README ReleaseNotes doc/*
%doc %{_mandir}/man?/*
/etc/bacula/bacula
/etc/bacula/console
/etc/bacula/fd
/etc/bacula/gconsole
/etc/bacula/create_mysql_database
/etc/bacula/make_mysql_tables
/etc/bacula/drop_mysql_tables
/etc/bacula/grant_mysql_privileges
/etc/bacula/make_bacula_tables
/etc/bacula/drop_bacula_tables
/etc/bacula/make_catalog_backup
/etc/bacula/delete_catalog_backup
/etc/bacula/startmysql
/etc/bacula/stopmysql
/etc/bacula/mtx-changer
/etc/init.d/bacula-dir
/etc/init.d/bacula-fd
/etc/init.d/bacula-sd

/usr/share/pixmaps/bacula.png
/usr/share/gnome/apps/System/bacula.desktop
/usr/share/applications/bacula.desktop
%config(noreplace) /etc/bacula/gnome-console.conf
/etc/logrotate.d/bacula

%config(noreplace) /etc/bacula/bacula-dir.conf
%config(noreplace) /etc/bacula/bacula-fd.conf
%config(noreplace) /etc/bacula/bacula-sd.conf
%config(noreplace) /etc/bacula/console.conf
/etc/bacula/query.sql
%dir %{working_dir}

/usr/sbin/*

%pre mysql

%post mysql

# add our links
if [ "$1" -ge 1 ] ; then
/sbin/chkconfig --add bacula-dir
/sbin/chkconfig --add bacula-fd
/sbin/chkconfig --add bacula-sd
fi

# test for an existing database
# note: this ASSUMES no password has been set for bacula database
DB_VER=`mysql bacula -e 'select * from Version;'|tail -n 1 2>/dev/null`

# grant privileges and create tables if they do not exist
if [ -z "$DB_VER" ]; then
	echo "Hmm, doesn't look like you have an existing database."
	echo "Granting privileges for MySQL user bacula..."
	/etc/bacula/grant_mysql_privileges
	echo "Creating MySQL bacula database..."
	/etc/bacula/create_mysql_database
	echo "Creating bacula tables..."
	/etc/bacula/make_mysql_tables
fi

%preun mysql
# delete our links
if [ $1 = 0 ]; then
/sbin/chkconfig --del bacula-dir
/sbin/chkconfig --del bacula-fd
/sbin/chkconfig --del bacula-sd
fi

%endif

%if %{sqlite}

%files sqlite
%defattr(-, root, root, 0755)

/etc/bacula/bacula
/etc/bacula/console
/etc/bacula/fd
/etc/bacula/gconsole
/etc/bacula/make_bacula_tables
/etc/bacula/drop_bacula_tables
/etc/bacula/create_sqlite_database
/etc/bacula/make_sqlite_tables
/etc/bacula/drop_sqlite_tables
/etc/bacula/make_catalog_backup
/etc/bacula/delete_catalog_backup
/etc/bacula/mtx-changer
/etc/init.d/bacula-dir
/etc/init.d/bacula-fd
/etc/init.d/bacula-sd

%doc COPYING ChangeLog INSTALL README ReleaseNotes doc/*
/usr/man/man1/*
/usr/share/pixmaps/bacula.png
/usr/share/gnome/apps/System/bacula.desktop
/usr/share/applications/bacula.desktop
%config(noreplace) /etc/bacula/gnome-console.conf
/etc/logrotate.d/bacula

%config(noreplace) /etc/bacula/bacula-dir.conf
%config(noreplace) /etc/bacula/bacula-fd.conf
%config(noreplace) /etc/bacula/bacula-sd.conf
%config(noreplace) /etc/bacula/console.conf
/etc/bacula/query.sql
%{sqlite_bindir}/libsqlite.a
%{sqlite_bindir}/sqlite.h
%dir %{working_dir}

/usr/sbin/*
%{sqlite_bindir}/sqlite

%pre sqlite

%post sqlite
# add our links
if [ "$1" -ge 1 ] ; then
/sbin/chkconfig --add bacula-dir
/sbin/chkconfig --add bacula-fd
/sbin/chkconfig --add bacula-sd
fi

# test for an existing database
if [ -s %{working_dir}/bacula.db ]; then
	DB_VER=`echo "select * from Version;" | %{sqlite_bindir}/sqlite %{working_dir}/bacula.db | tail -n 1 2>/dev/null`
else
	# create the database and tables
	echo "Hmm, doesn't look like you have an existing database."
	echo "Creating SQLite database..."
	/etc/bacula/create_sqlite_database
	echo "Creating the SQLite tables..."
	/etc/bacula/make_sqlite_tables
fi

%preun sqlite
# delete our links
if [ $1 = 0 ]; then
/sbin/chkconfig --del bacula-dir
/sbin/chkconfig --del bacula-fd
/sbin/chkconfig --del bacula-sd
fi

%endif

%files client
%defattr(-, root, root, 0755)
/etc/bacula/fd
/etc/bacula/console
/etc/init.d/bacula-fd

%doc COPYING ChangeLog INSTALL README ReleaseNotes doc/*
/etc/logrotate.d/bacula

%config(noreplace) /etc/bacula/bacula-fd.conf
%config(noreplace) /etc/bacula/console.conf
%dir %{working_dir}

/usr/sbin/bacula-fd
/usr/sbin/btraceback
/usr/sbin/btraceback.gdb
/usr/sbin/smtp
/usr/sbin/console


%post client
# add our link
if [ "$1" -ge 1 ] ; then
/sbin/chkconfig --add bacula-fd
fi

%preun client
# delete our link
if [ $1 = 0 ]; then
/sbin/chkconfig --del bacula-fd
fi

%files rescue
%defattr(-, root, root, 0755)
/etc/bacula/rescue/backup.etc.list
/etc/bacula/rescue/format_floppy
/etc/bacula/rescue/getdiskinfo
/etc/bacula/rescue/make_rescue_disk
/etc/bacula/rescue/restore_bacula
/etc/bacula/rescue/restore_etc
/etc/bacula/rescue/run_grub
/etc/bacula/rescue/run_lilo
/etc/bacula/rescue/sfdisk.bz2
/etc/bacula/rescue/bacula-fd
/etc/bacula/rescue/tomsrtbt/*

%post rescue
# link our current installed conf file to the rescue directory
ln -s /etc/bacula-fd.conf /etc/bacula/rescue/bacula-fd.conf

# run getdiskinfo
echo "Creating rescue files for this system..."
cd /etc/bacula/rescue
./getdiskinfo

%preun rescue
# remove the files created after the initial rpm installation
rm -f /etc/bacula/rescue/bacula-fd.conf
rm -f /etc/bacula/rescue/partition.*
rm -f /etc/bacula/rescue/format.*
rm -f /etc/bacula/rescue/mount_drives
rm -f /etc/bacula/rescue/start_network
rm -f /etc/bacula/rescue/sfdisk
rm -rf /etc/bacula/rescue/diskinfo/*

%files gconsole
%defattr(-, root, root, 0755)
%config(noreplace) /etc/bacula/gnome-console.conf
%config /etc/bacula/gconsole
%{_sbindir}/gnome-console
%{_datadir}/pixmaps/bacula.png
%{_datadir}/gnome/apps/System/bacula.desktop
%{_datadir}/applications/bacula.desktop

%changelog
* Mon Mar 29 2004 Dag Wieers <dag@wieers.com> - 1.32-1.f
- Initial package. (using DAR)
